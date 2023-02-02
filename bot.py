import logging
import praw
import prawcore
import templates
import utils

from praw.models import Comment
from urllib.error import HTTPError


handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
for logger_name in ("praw", "prawcore"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)


reddit = praw.Reddit("bot")


def handle_stream(i = None, reply = None):
  if i == None:
    for item in reddit.inbox.stream():
      try:
        # if item is not a mention, do nothing.
        if not isinstance(item, Comment):
          continue

        # parent_id follows this format t1_XXXXXXX or t3_XXXXXXX.
        splitted = item.parent_id.split("_", 1)

        # t3 means it is a top level comment, its parent is a submission.
        if splitted[0] == "t3":
          # print(f"[PARENT_ID (Submission): {splitted[0]}_{splitted[1]}] - [AUTHOR: {item.author}] - [ID: {item.id}] - [BODY: {item.body}]")
          parent_submission = reddit.submission(splitted[1])

          if parent_submission.is_self == False:
            firstLink = templates.first_option.format(parent_submission.url)
            secondLink = templates.second_option.format(parent_submission.url)
            reply_text = templates.fixed_template.format(firstLink, secondLink)
            res = item.reply(reply_text)
            if not res == None:
              print("[REPLY_ID]:", res)
              print(f"\n")

          else:
            list = utils.regex_find(parent_submission.selftext)
            reply_text = utils.build_reply_text(list)
            res = item.reply(reply_text)
            if not res == None:
              print("[REPLY_ID]:", res)
              print(f"\n")

        # t1 means its parent is a comment.
        if splitted[0] == "t1":
          # print(f"[PARENT_ID (Comment): {splitted[0]}_{splitted[1]}] - [AUTHOR: {item.author}] - [ID: {item.id}] - [BODY: {item.body}]")
          parent_comment = reddit.comment(splitted[1])

          list = utils.regex_find(parent_comment.body)
          reply_text = utils.build_reply_text(list)
          res = item.reply(reply_text)
          if not res == None:
            print("[REPLY_ID]:", res)
            print(f"\n")

      except HTTPError as err:
        print(err)
      except prawcore.exceptions.Forbidden as err:
        print(err)
        print(f"\n")
        continue
      except praw.exceptions.RedditAPIException as err:
        print(err)
        handle_stream(item, reply_text)
      else:
        item.mark_read()
  else:
    res = i.reply(reply)
    if not res == None:
      print("[REPLY_ID]:", res)
      print(f"\n")
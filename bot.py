"""Module bot. Implement BOT itself."""
import logging
from urllib.error import HTTPError
import praw
import prawcore
from praw.models import Comment
import templates
import utils


handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
for logger_name in ("praw", "prawcore"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)


reddit = praw.Reddit("bot")


# pylint: disable-next=too-many-branches
def handle_stream(i = None, reply = None):
    """handle_stream function implements the function which
    will handle the inbox stream of mentions and reply to them.
    """
    # pylint: disable-next=too-many-nested-blocks
    if i is None:
        for item in reddit.inbox.stream():
            try:
                # if item is not a mention, do nothing.
                if not isinstance(item, Comment):
                    continue

                # parent_id follows this format t1_XXXXXXX or t3_XXXXXXX.
                splitted = item.parent_id.split("_", 1)

                # t3 means it is a top level comment, its parent is a submission.
                if splitted[0] == "t3":
                    # print(
                      # f"[PARENT_ID (Submission): {splitted[0]}_{splitted[1]}]
                      # [AUTHOR: {item.author}]
                      # [ID: {item.id}]
                      # [BODY: {item.body}]"
                    # )
                    parent_submission = reddit.submission(splitted[1])

                    if not parent_submission.is_self:
                        first_link = templates.FIRST_OPTION.format(parent_submission.url)
                        second_link = templates.SECOND_OPTION.format(parent_submission.url)
                        reply_text = templates.FIXED_TEMPLATE.format(first_link, second_link)
                        res = item.reply(reply_text)
                        if not res is None:
                            print("[REPLY_ID]:", res)

                    else:
                        link_list = utils.regex_find(parent_submission.selftext)
                        reply_text = utils.build_reply_text(link_list)
                        res = item.reply(reply_text)
                        if not res is None:
                            print("[REPLY_ID]:", res)

                # t1 means its parent is a comment.
                if splitted[0] == "t1":
                    # print(
                      # f"[PARENT_ID (Comment): {splitted[0]}_{splitted[1]}]
                      # [AUTHOR: {item.author}]
                      # [ID: {item.id}]
                      # [BODY: {item.body}]"
                    # )
                    parent_comment = reddit.comment(splitted[1])

                    link_list = utils.regex_find(parent_comment.body)
                    reply_text = utils.build_reply_text(link_list)
                    res = item.reply(reply_text)
                    if not res is None:
                        print("[REPLY_ID]:", res)

            except HTTPError as err:
                print(err)
            except prawcore.exceptions.Forbidden as err:
                print(err)
                continue
            except praw.exceptions.RedditAPIException as err:
                print(err)
                handle_stream(item, reply_text)
            else:
                item.mark_read()
    else:
        res = i.reply(reply)
        if not res is None:
            print("[REPLY_ID]:", res)

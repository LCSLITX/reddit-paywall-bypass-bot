"""Module bot. Implement BOT itself."""
from urllib.error import HTTPError
import configparser
import os
import praw
import prawcore
from praw.models import Comment
from src import templates
from src import utils


config = configparser.ConfigParser()
config.read('praw.ini')


debug_mode = config.get("DEFAULT", "REDDIT_BOT_DEBUG_MODE", vars=os.environ)
print("REDDIT_BOT_DEBUG_MODE:", debug_mode)
if debug_mode == "True":
    utils.debug_mode()


reddit = praw.Reddit(
    client_id=config.get("BOT", "REDDIT_BOT_CLIENT_ID", vars=os.environ),
    client_secret=config.get("BOT", "REDDIT_BOT_CLIENT_SECRET", vars=os.environ),
    username=config.get("BOT", "REDDIT_BOT_USERNAME", vars=os.environ),
    password=config.get("BOT", "REDDIT_BOT_PASSWORD", vars=os.environ),
    user_agent="USER_AGENT",
    rate_limit=300
    )


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
                    parent_submission = reddit.submission(splitted[1])
                    # is_self is true when submission have self_text.
                    if parent_submission.is_self:
                        no_link_list = utils.regex_find_markdown_link(parent_submission.selftext)
                        link_list = utils.regex_find_url(no_link_list)
                        reply_text = utils.build_reply_text(link_list)
                        res = item.reply(reply_text)
                        if not res is None:
                            print("[REPLY_ID]:", res)
                    else:
                        first_link = templates.FIRST_OPTION.format(parent_submission.url)
                        second_link = templates.SECOND_OPTION.format(parent_submission.url)
                        reply_text = templates.NOT_SELFTEXT_TEMPLATE.format(first_link, second_link)
                        res = item.reply(reply_text)
                        if not res is None:
                            print("[REPLY_ID]:", res)

                # t1 means its parent is a comment.
                if splitted[0] == "t1":
                    parent_comment = reddit.comment(splitted[1])

                    no_link_list = utils.regex_find_markdown_link(parent_comment.body)
                    link_list = utils.regex_find_url(no_link_list)
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

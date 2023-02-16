"""Module bot. Implement BOT itself."""
from urllib.error import HTTPError
import praw
import prawcore
from praw.models import Comment
from src import utils
from src import reddit as r


def handle_stream() -> None:
    """handle_stream function implements the function which
    will handle the inbox stream of mentions and reply to them.
    """
    for item in r.reddit_instance.inbox.stream():
        # if item is not a mention, do nothing.
        if not isinstance(item, Comment):
            continue
        try:
            reply_text = define_reply(item)
            reply(item, reply_text)
        except HTTPError as err:
            print(err)
        except prawcore.exceptions.Forbidden as exception:
            print(exception)
            continue
        except praw.exceptions.RedditAPIException as exception:
            # for subexception in exception.items:
            #     print(subexception)
            print(exception)
            reply(item, reply_text)
        except praw.exceptions.ClientException as exception:
            print(exception)
        else:
            item.mark_read()


def define_reply(item: Comment) -> str:
    """define_reply function receives an item, triaging it, 
    defining its reply template and building it."""
    [parent_type, parent_id] = utils.get_parent_id(item.parent_id)
    # t3 means submission
    if parent_type == "t3":
        parent_submission = r.reddit_instance.submission(parent_id)
        # is_self is true when submission have self_text.
        if parent_submission.is_self:
            link_list = utils.get_links(parent_submission.selftext)
            return utils.build_reply_text(link_list)

        return utils.build_reply_text([ *parent_submission.url ])

    # t1 means comment
    if parent_type == "t1":
        parent_comment = r.reddit_instance.comment(parent_id)
        link_list = utils.get_links(parent_comment.selftext)
        return utils.build_reply_text(link_list)


def reply(item: Comment, message: str) -> None:
    """reply function receives an item (submission or comment) and reply to it."""
    res = item.reply(message)
    if not res is None:
        print("[REPLY_ID]:", res)

"""bot_test.py provides tests to bot module."""
from praw.models import Comment
from src import bot
from src import templates
from src import reddit as r
from tests import templates as tt

def test_define_reply():
    """test_define_reply function tests define_reply() functionality."""
    # pylint: disable=line-too-long

    # parent_submission.is_self = True
    # https://www.reddit.com/r/test/comments/10rpgpm/comment/j8rtss2/?utm_source=share&utm_medium=web2x&context=3
    expected1 = f"{templates.REPLY_TEMPLATE}{tt.EXPECTED_LINKS}{templates.BYE_BYE_TEMPLATE}"
    item = Comment(r.read_only_reddit_instance, "j8rtss2")
    string1 = bot.define_reply(item)
    assert string1 == expected1


    # parent_submission.is_self = False
    # https://www.reddit.com/r/test/comments/113w28m/comment/j8sk27z/
    expected2 = f"{templates.REPLY_TEMPLATE}{tt.EXPECTED_LINK}{templates.BYE_BYE_TEMPLATE}"
    item2 = Comment(r.read_only_reddit_instance, "j8sk27z")
    string2 = bot.define_reply(item2)
    assert string2 == expected2


    # # parent_comment
    # https://www.reddit.com/r/test/comments/10rpgpm/comment/j8sibb1/?utm_source=share&utm_medium=web2x&context=3
    item3 = Comment(r.read_only_reddit_instance, "j8sibb1")
    string3 = bot.define_reply(item3)
    assert string3 == expected1


    # parent_comment
    # https://www.reddit.com/r/test/comments/10rpgpm/comment/j8t2dm9/?utm_source=share&utm_medium=web2x&context=3
    item4 = Comment(r.read_only_reddit_instance, "j8t2dm9")
    string4 = bot.define_reply(item4)
    assert string4 == expected2


    # deleted comment
    # https://www.reddit.com/r/undefined/comments/113xrp8/comment/j8szj5q/?utm_source=share&utm_medium=web2x&context=3
    expected5 = f"{templates.NO_LINKS_TEMPLATE}{templates.BYE_BYE_TEMPLATE}"
    item5 = Comment(r.read_only_reddit_instance, "j8szj5q")
    string5 = bot.define_reply(item5)
    assert string5 == expected5


    # own comment
    # https://www.reddit.com/r/brdev/comments/1151rhx/comment/j8z5n0k/?utm_source=share&utm_medium=web2x&context=3
    expected5 = ""
    item5 = Comment(r.read_only_reddit_instance, "j8z5n0k")
    string5 = bot.define_reply(item5)
    assert string5 == expected5


    # own submission
    # https://www.reddit.com/r/brdev/comments/1151rhx/comment/j8z5hc2/?utm_source=share&utm_medium=web2x&context=3
    expected5 = f"{templates.REPLY_TEMPLATE}{tt.EXPECTED_LINKS2}{templates.BYE_BYE_TEMPLATE}"
    item6 = Comment(r.read_only_reddit_instance, "j8z5hc2")
    string6 = bot.define_reply(item6)
    assert string6 == expected5

# pylint: enable=line-too-long

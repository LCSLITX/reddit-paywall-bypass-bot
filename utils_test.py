"""tests.py provides tests to whole project."""
import utils
import templates

# pylint: disable=line-too-long
SELFTEXT_WITH_THREE_LINKS = r"Donec quis justo sed elit pellentesque tristique. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In ut blandit nibh, et pharetra ex.\
\
**Generated 3 paragraphs, 280 words, 1912 bytes of** [**Lorem Ipsum**](https://www.lipsum.com/) \
\
[https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker\_group\_releases\_128gb\_of\_data\_showing/](https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/)  \
\
[PRAW](https://praw.readthedocs.io/en/stable/)"

SELFTEXT_WITH_FOUR_LINKS = r"Donec quis justo sed elit pellentesque tristique. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In ut blandit nibh, et pharetra ex.\
\
**Generated 3 paragraphs, 280 words, 1912 bytes of** [**Lorem Ipsum**](https://www.lipsum.com/) \
\
[https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker\_group\_releases\_128gb\_of\_data\_showing/](https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/)  \
\
[google](http://google.com) \
\
[PRAW](https://praw.readthedocs.io/en/stable/)"

SELFTEXT_WITHOUT_LINKS = "Donec quis justo sed elit pellentesque tristique. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In ut blandit nibh, et pharetra ex."

expected_markdown_links = [
    r"[**Lorem Ipsum**](https://www.lipsum.com/)",
    r"[https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker\_group\_releases\_128gb\_of\_data\_showing/](https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/)",
    r"[PRAW](https://praw.readthedocs.io/en/stable/)",
]

expected_urls = [
    "https://www.lipsum.com/",
    "https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/",
    "https://praw.readthedocs.io/en/stable/",
]


def test_regex_find_markdown_link():
    """test_regex_find_markdown_link function tests regex_find_markdown_link() functionality."""
    for index, elem in enumerate(utils.regex_find_markdown_link(SELFTEXT_WITH_THREE_LINKS)):
        assert f"{elem}" == expected_markdown_links[index]
    assert utils.regex_find_markdown_link(SELFTEXT_WITH_THREE_LINKS) == expected_markdown_links


def test_regex_find_url():
    """test_regex_find function tests regex_find() functionality."""
    for index, elem in enumerate(utils.regex_find_url(expected_markdown_links)):
        assert f"{elem}" == expected_urls[index]
    assert utils.regex_find_url(expected_markdown_links) == expected_urls


def test_build_reply_text():
    """test_build_reply_text function tests build_reply_text() functionality."""
    expected_links1 = "1º Link: [First Option](https://12ft.io/https://www.lipsum.com/); [Second Option](https://www.removepaywall.com/https://www.lipsum.com/)\n\
\n\
2º Link: [First Option](https://12ft.io/https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/); [Second Option](https://www.removepaywall.com/https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/)\n\
\n\
3º Link: [First Option](https://12ft.io/https://praw.readthedocs.io/en/stable/); [Second Option](https://www.removepaywall.com/https://praw.readthedocs.io/en/stable/)\n\
\n"
    expected1 = f"{templates.SELFTEXT_TEMPLATE}{expected_links1}{templates.BYE_BYE_TEMPLATE}"
    no_link_list1 = utils.regex_find_markdown_link(SELFTEXT_WITH_THREE_LINKS)
    link_list1 = utils.regex_find_url(no_link_list1)
    reply_text1 = utils.build_reply_text(link_list1)
    assert reply_text1 == expected1

    expected_links2 = "1º Link: [First Option](https://12ft.io/https://www.lipsum.com/); [Second Option](https://www.removepaywall.com/https://www.lipsum.com/)\n\
\n\
2º Link: [First Option](https://12ft.io/https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/); [Second Option](https://www.removepaywall.com/https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/)\n\
\n\
3º Link: [First Option](https://12ft.io/http://google.com); [Second Option](https://www.removepaywall.com/http://google.com)\n\
\n\
I verified that there are more links, but I can only bypass three. Good luck with the rest.\n\
\n"
    expected2 = f"{templates.SELFTEXT_TEMPLATE}{expected_links2}{templates.BYE_BYE_TEMPLATE}"
    no_link_list2 = utils.regex_find_markdown_link(SELFTEXT_WITH_FOUR_LINKS)
    link_list2 = utils.regex_find_url(no_link_list2)
    reply_text2 = utils.build_reply_text(link_list2)
    assert reply_text2 == expected2

    no_link_list3 = utils.regex_find_markdown_link(SELFTEXT_WITHOUT_LINKS)
    link_list3 = utils.regex_find_url(no_link_list3)
    reply_text3 = utils.build_reply_text(link_list3)
    assert reply_text3 == templates.NO_LINKS_TEMPLATE

# pylint: enable=line-too-long

"""tests.py provides tests to whole project."""
import utils

# pylint: disable=line-too-long
SELFTEXT_WITH_THREE_LINKS = r"Donec quis justo sed elit pellentesque tristique. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In ut blandit nibh, et pharetra ex. Aenean lobortis justo vel augue tristique, vitae auctor massa eleifend. Cras lobortis nulla sit amet leo malesuada efficitur. Duis volutpat ipsum id nulla congue posuere. Nam sit amet purus at metus sollicitudin lacinia eu quis erat. Praesent dui orci, aliquet maximus egestas nec, bibendum a quam. Curabitur ligula sem, consequat et commodo a, rhoncus sit amet diam. Mauris vehicula orci neque, eget viverra odio sollicitudin sed. Aenean vitae faucibus tortor, sit amet malesuada massa. Vestibulum ullamcorper nibh ut orci pulvinar porttitor. Suspendisse fermentum nunc vel dolor congue, sit amet tincidunt felis molestie.\
\
**Generated 3 paragraphs, 280 words, 1912 bytes of** [**Lorem Ipsum**](https://www.lipsum.com/) \
\
[https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker\_group\_releases\_128gb\_of\_data\_showing/](https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/)  \
\
[PRAW](https://praw.readthedocs.io/en/stable/)"

SELFTEXT_WITH_FOUR_LINKS = r"Donec quis justo sed elit pellentesque tristique. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In ut blandit nibh, et pharetra ex. Aenean lobortis justo vel augue tristique, vitae auctor massa eleifend. Cras lobortis nulla sit amet leo malesuada efficitur. Duis volutpat ipsum id nulla congue posuere. Nam sit amet purus at metus sollicitudin lacinia eu quis erat. Praesent dui orci, aliquet maximus egestas nec, bibendum a quam. Curabitur ligula sem, consequat et commodo a, rhoncus sit amet diam. Mauris vehicula orci neque, eget viverra odio sollicitudin sed. Aenean vitae faucibus tortor, sit amet malesuada massa. Vestibulum ullamcorper nibh ut orci pulvinar porttitor. Suspendisse fermentum nunc vel dolor congue, sit amet tincidunt felis molestie.\
\
**Generated 3 paragraphs, 280 words, 1912 bytes of** [**Lorem Ipsum**](https://www.lipsum.com/) \
\
[https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker\_group\_releases\_128gb\_of\_data\_showing/](https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/)  \
\
[google](http://google.com) \
\
[PRAW](https://praw.readthedocs.io/en/stable/)"

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
    expected1 = "Beep Beep. I'm a BOT who doesn't like Paywalls. 🤖\n\
\n\
I do provide alternative links so you can read your news or articles without those annoying things.\n\
\n\
Here are your links:\
\n\
\n\
1º Link: [First Option](https://12ft.io/https://www.lipsum.com/); [Second Option](https://www.removepaywall.com/https://www.lipsum.com/)\n\
\n\
2º Link: [First Option](https://12ft.io/https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/); [Second Option](https://www.removepaywall.com/https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/)\n\
\n\
3º Link: [First Option](https://12ft.io/https://praw.readthedocs.io/en/stable/); [Second Option](https://www.removepaywall.com/https://praw.readthedocs.io/en/stable/)\n\
\n\
Beep beep. Bye."
    no_link_list = utils.regex_find_markdown_link(SELFTEXT_WITH_THREE_LINKS)
    link_list = utils.regex_find_url(no_link_list)
    reply_text = utils.build_reply_text(link_list)
    assert reply_text == expected1

    expected2 = "Beep Beep. I'm a BOT who doesn't like Paywalls. 🤖\n\
\n\
I do provide alternative links so you can read your news or articles without those annoying things.\n\
\n\
Here are your links:\
\n\
\n\
1º Link: [First Option](https://12ft.io/https://www.lipsum.com/); [Second Option](https://www.removepaywall.com/https://www.lipsum.com/)\n\
\n\
2º Link: [First Option](https://12ft.io/https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/); [Second Option](https://www.removepaywall.com/https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/)\n\
\n\
3º Link: [First Option](https://12ft.io/http://google.com); [Second Option](https://www.removepaywall.com/http://google.com)\n\
\n\
I verified that there are more links, but I can only bypass three. Good luck with the rest.\n\
\n\
Beep beep. Bye."
    no_link_list = utils.regex_find_markdown_link(SELFTEXT_WITH_FOUR_LINKS)
    link_list = utils.regex_find_url(no_link_list)
    reply_text = utils.build_reply_text(link_list)
    assert reply_text == expected2

# pylint: enable=line-too-long

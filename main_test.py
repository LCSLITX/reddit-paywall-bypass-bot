"""tests.py provides tests to whole project."""

import utils

# integration test of utils
def test_regex_find():
    """test_regex_find function tests regex_find() functionality."""
    # pylint: disable=line-too-long
    self_text = r"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam porta luctus tempor. Pellentesque consectetur imperdiet vestibulum. Integer eget orci sit amet est porta sagittis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus eu nibh lobortis, porta nulla eu, porta urna. Nunc purus sapien, imperdiet id ipsum vel, ultricies vehicula ex. Donec metus diam, varius porta odio condimentum, pellentesque posuere lacus. Vestibulum vel mauris pretium, congue tellus quis, congue mauris. Mauris non diam pharetra, dignissim nunc id, laoreet risus. Curabitur euismod nunc nec sagittis congue.\
    \
    Donec ut felis ac quam sagittis bibendum. Curabitur aliquam pharetra nulla a ullamcorper. Ut dictum pretium dolor, id faucibus elit. Quisque id velit non odio vulputate bibendum eget ut mauris. Nam vitae leo ut magna dapibus pulvinar in vulputate tortor. Maecenas pellentesque ex quis purus pulvinar, ut cursus augue blandit. Sed a purus aliquet nisl rhoncus placerat. Fusce sit amet dapibus arcu. Donec nisl lorem, sollicitudin facilisis sollicitudin tempus, fringilla ut turpis.\
    \
    Donec quis justo sed elit pellentesque tristique. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In ut blandit nibh, et pharetra ex. Aenean lobortis justo vel augue tristique, vitae auctor massa eleifend. Cras lobortis nulla sit amet leo malesuada efficitur. Duis volutpat ipsum id nulla congue posuere. Nam sit amet purus at metus sollicitudin lacinia eu quis erat. Praesent dui orci, aliquet maximus egestas nec, bibendum a quam. Curabitur ligula sem, consequat et commodo a, rhoncus sit amet diam. Mauris vehicula orci neque, eget viverra odio sollicitudin sed. Aenean vitae faucibus tortor, sit amet malesuada massa. Vestibulum ullamcorper nibh ut orci pulvinar porttitor. Suspendisse fermentum nunc vel dolor congue, sit amet tincidunt felis molestie.\
    \
    **Generated 3 paragraphs, 280 words, 1912 bytes of** [**Lorem Ipsum**](https://www.lipsum.com/) \ "
    # \
    # [https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker\_group\_releases\_128gb\_of\_data\_showing/](https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/)  \
    # \ "
    # \
    # [PRAW](https://praw.readthedocs.io/en/stable/)"

    expected = [
        "https://www.lipsum.com/",
        # pylint: disable-next=line-too-long
        # "https://www.reddit.com/r/worldnews/comments/10ri0wu/hacker_group_releases_128gb_of_data_showing/",
        # "https://praw.readthedocs.io/en/stable/",
    ]

    # pylint: enable=line-too-long
    assert utils.regex_find(self_text) == expected

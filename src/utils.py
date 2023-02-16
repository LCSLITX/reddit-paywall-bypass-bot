
"""Module utils. Provides utilitary functions."""
import re
import logging
from src import templates


def regex_get_markdown_links(self_text: str) -> list[str]:
    """regex_get_markdown_links function checks a string for regex pattern
    and returns a list with all correspondences in markdown format.
    """
    return re.findall(templates.REGEX_PATTERN_MD_LINK, self_text)


def regex_get_url(markdown_link_list):
    """regex_get_url function checks a list of mardown formatted links
    and returns a list with only URLs.
    """
    link_list = []
    for url in markdown_link_list:
        matched_md = re.search(templates.REGEX_PATTERN_URL, url)
        url = matched_md.group().lstrip("(").rstrip(")")
        link_list.append(url)
    return link_list


def build_reply_text(link_list: list[str]) -> str:
    """build_reply_text function builds a string to be used as a reply text."""
    if len(link_list) == 0:
        return templates.NO_LINKS_TEMPLATE

    if len(link_list) == 1:
        return templates.NOT_SELFTEXT_TEMPLATE.format(
            templates.FIRST_OPTION.format(link_list[0]),
            templates.SECOND_OPTION.format(link_list[0])
        )

    reply_text = templates.SELFTEXT_TEMPLATE

    for index, url in enumerate(link_list):
        if index >= 3:
            reply_text += templates.MANY_LINKS_TEMPLATE
            break
        # pylint: disable-next=line-too-long
        reply_text += f"{index + 1}º Link: {templates.FIRST_OPTION.format(url)}; {templates.SECOND_OPTION.format(url)}\n\
\n\
"
    reply_text += templates.BYE_BYE_TEMPLATE
    return reply_text


def get_parent_id(parent_id: str) -> list[str]:
    """get_parent_id function receives a string and split it 
    to obtain type and id of a parent submission or comment. \n
    parent_id follows this format t1_XXXXXXX or t3_XXXXXXX. \n
    t3 means it is a top level comment, its parent is a submission. \n
    t1 means its parent is a comment.
    """
    splitted = parent_id.split("_", 1)
    return splitted


def get_links(self_text: str) -> list[str]:
    """get_links function receives a string, looks over it
    for links and return them in a list.
    """
    markdown_formated_link_list = regex_get_markdown_links(self_text)
    link_list = regex_get_url(markdown_formated_link_list)
    return link_list


def debug_mode():
    """debug_mode function implements the function which
    will activate and log info for when mode bool is set to True.
    """
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    for logger_name in ("praw", "prawcore"):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)


"""Module utils. Provides utilitary functions."""
import re
import logging
from src import templates


def regex_get_markdown_links(self_text: str) -> list[str]:
    """regex_get_markdown_links function checks a string for regex pattern
    and returns a list with all correspondences in markdown format.
    """
    return re.findall(templates.REGEX_PATTERN_URL_MD_WRAPPED, self_text)


def regex_get_url(markdown_link_list) -> list[str]:
    """regex_get_url function checks a list of mardown formatted links
    and returns a list with only URLs.
    """
    link_list = []
    for url in markdown_link_list:
        matched_md = re.search(templates.REGEX_PATTERN_URL_PARENTHESIS_WRAPPED, url)
        url = matched_md.group().lstrip("(").rstrip(")")
        link_list.append(url)
    return link_list


def regex_redundant(self_text: str) -> list[str]:
    """regex_redundant function is supposed to be called redundantly and
    checks a string for regex pattern and returns a list with all correspondences 
    in markdown format.

    This function is needed as there is some situations which the user submit a comment
    containing a link with Reddit's Fancy Pants Editor and the link, supposedly, is not formatted 
    in the backend to markdown. So parent_comment.body, which is supposed to return the markdown
    formatted comment does return plain text, instead. Due to this regex_get_markdown_links function
    is not capable of detecting the link.
    """
    return re.findall(templates.REGEX_PATTERN_URL_NO_WRAP, self_text)


def build_reply_text(link_list: list[str]) -> str:
    """build_reply_text function builds a string to be used as a reply text."""
    if len(link_list) == 0:
        reply_text = templates.NO_LINKS_TEMPLATE

    else:
        reply_text = templates.REPLY_TEMPLATE

        for index, url in enumerate(link_list):
            if index >= 3:
                reply_text += templates.MANY_LINKS_TEMPLATE
                break
            # pylint: disable-next=line-too-long
            reply_text += f"{index + 1}º Link: {templates.FIRST_OPTION.format(url)}; {templates.SECOND_OPTION.format(url)}\n\n"

    reply_text += templates.BYE_BYE_TEMPLATE
    return reply_text


def get_parent_id(fullname: str) -> list[str]:
    """get_parent_id function receives a fullname string and split it 
    to obtain type and id of a parent submission or comment. \n
    fullname follows a specific format. The first two characters varies from t1 to t6,
    the third is always an underscore that works as a separator, and the rest is a base-36 id.
    The fullnames that matters for this application are t1_XXXXXXX and t3_XXXXXXX. \n
    t3 means it is a top level comment, its parent is necessarily a submission. \n
    t1 means it is a subcomment, its parent is necessarily a comment.
    """
    fullname_splitted = fullname.split("_", 1)
    return fullname_splitted


def get_links(self_text: str) -> list[str]:
    """get_links function receives a string, looks over it
    for links and return them in a list.
    """
    markdown_formated_link_list = regex_get_markdown_links(self_text)
    link_list = regex_get_url(markdown_formated_link_list)
    if len(link_list) == 0:
        link_list = regex_redundant(self_text)
    return link_list


def debug_mode() -> None:
    """debug_mode function implements the function which
    will activate and log info for when mode bool is set to True.
    """
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    for logger_name in ("praw", "prawcore"):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)

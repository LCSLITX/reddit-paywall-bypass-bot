
"""Module utils. Provides utilitary functions."""
import re
import logging
from src import templates


def regex_find_markdown_link(text):
    """regex_find_markdown_link function checks a string for regex pattern
    and returns a list with all correspondences in markdown format.
    """
    return re.findall(templates.REGEX_PATTERN_MD_LINK, text)


def regex_find_url(markdown_link_list):
    """regex_find_url function checks a list of mardown formatted links
    and returns a list with only URLs.
    """
    link_list = []
    for url in markdown_link_list:
        matched_md = re.search(templates.REGEX_PATTERN_URL, url)
        link = matched_md.group().lstrip("(").rstrip(")")
        link_list.append(link)
    return link_list


def build_reply_text(link_list):
    """build_reply_text function builds a string to be used as a reply text."""
    if len(link_list) == 0:
        return templates.NO_LINKS_TEMPLATE
    reply_text = templates.SELFTEXT_TEMPLATE
    for index, url in enumerate(link_list):
        if index >= 3:
            reply_text += templates.MANY_LINKS_TEMPLATE
            break
        # pylint: disable-next=line-too-long
        reply_text += f"{index + 1}º Link: [First Option]({templates.MULTI_FIRST_OPTION.format(url)}); [Second Option]({templates.MULTI_SECOND_OPTION.format(url)})\n\
\n\
"
    reply_text += templates.BYE_BYE_TEMPLATE
    return reply_text


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

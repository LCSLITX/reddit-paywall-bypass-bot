
"""Module utils. Provides utilitary functions."""

import re
import templates


def regex_find(text):
    """regex_find function checks a string for regex pattern
    and returns a list with all correspondences.
    """
    reg = re.findall(templates.REGEX_PATTERN, text)
    for index, elem in enumerate(reg):
        reg[index] = elem.rstrip(")")
    return reg


def build_reply_text(link_list):
    """build_reply_text function builds a string to be used as a reply text."""
    reply_text = templates.DYNAMIC_TEMPLATE

    for index, url in enumerate(link_list):
        if index >= 3:
            break
        # pylint: disable-next=line-too-long
        reply_text += f"{index + 1}º Link: [First Option]({templates.MULTI_FIRST_OPTION.format(url)}); [Second Option]({templates.MULTI_SECOND_OPTION.format(url)})  \n \
\n \
"
    reply_text += "Beep beep. Bye."

    return reply_text

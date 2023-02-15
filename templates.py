"""Module templates. Provides all templates to be used by BOT."""


# the indentation is intentional.
# The string should not use tabs to not broke markdown text when sent with request.
SELFTEXT_TEMPLATE = "Beep Beep. I'm a BOT who doesn't like Paywalls. 🤖\n\
\n\
I do provide alternative links so you can read your news or articles without those annoying things.\n\
\n\
Here are your links:\
\n\
\n\
"
# the indentation is intentional.
# The string should not use tabs to not broke markdown text when sent with request.
NOT_SELFTEXT_TEMPLATE = "Beep Beep. I'm a BOT who doesn't like Paywalls. 🤖\n\
\n\
I do provide alternative links so you can read your news or articles without those annoying things.\n\
\n\
Here are your links:\
\n\
\n\
- {}\
\n\
\n\
- {}\
\n\
\n\
Beep beep. Bye."

# pylint: disable-next=line-too-long
MANY_LINKS_TEMPLATE = "I verified that there are more links, but I can only bypass three. Good luck with the rest.\n\
\n"

BYE_BYE_TEMPLATE = "Beep beep. Bye."

NO_LINKS_TEMPLATE = "Beep Beep. I'm a BOT who doesn't like Paywalls. 🤖\n\
\n\
I do provide alternative links so you can read your news or articles without those annoying things.\n\
\n\
Unfortunately, I didn't find any links to bypass.\n\
\n\
Beep beep. Bye."

FIRST_OPTION = "[First option](https://12ft.io/{})"
SECOND_OPTION = "[Second option](https://www.removepaywall.com/{})"

MULTI_FIRST_OPTION = "https://12ft.io/{}"
MULTI_SECOND_OPTION = "https://www.removepaywall.com/{}"

# works at Regexr, but re.findall() return tuples when regex has capturing groups:
# REGEX_PATTERN = r"\[(.+)?\]\(((?:\/|https?:\/\/).+)\)"

#  without capturing groups re.findall() returns a list of correspondent strings:
REGEX_PATTERN_MD_LINK = r"\[(?:.+)?\]\((?:\/|https?:\/\/.+)\)"

REGEX_PATTERN_URL = r"\(((?:\/|https?:\/\/).+)\)"

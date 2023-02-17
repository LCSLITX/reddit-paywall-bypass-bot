"""Module templates. Provides all templates to be used by BOT."""


# the indentation is intentional.
# The string should not use tabs to not broke markdown text when sent with request.
REPLY_TEMPLATE = "Beep Beep. I'm a BOT who doesn't like Paywalls. 🤖\n\n\
I do provide alternative links so you can read your news or articles without those annoying things.\n\n\
Here are your links:\n\n"


# pylint: disable-next=line-too-long
MANY_LINKS_TEMPLATE = "I verified that there are more links, but I can only bypass three. Good luck with the rest.\n\n"


BYE_BYE_TEMPLATE = "Beep beep. Bye.\n\n\
[How to use](https://www.reddit.com/user/PaywallBypassBOT/comments/113xrp8/how_to_use_it/) \
| [Source code](https://github.com/lucassauro/reddit-paywall-bypass-bot) \
| [Report a bug](https://github.com/lucassauro/reddit-paywall-bypass-bot/issues/new) \
| [Feedback](https://www.reddit.com/message/compose/?to=PaywallBypassBOT)"


NO_LINKS_TEMPLATE = "Beep Beep. I'm a BOT who doesn't like Paywalls. 🤖\n\n\
I do provide alternative links so you can read your news or articles without those annoying things.\n\n\
Unfortunately, I didn't find any links to bypass.\n\n"


# PAYWALL BYPASS PROVIDERS
FIRST_OPTION = "[First Option](https://www.removepaywall.com/{})"
SECOND_OPTION = "[Second Option](https://12ft.io/{})"


# REGEX PATTERNS
# works at Regexr, but re.findall() return tuples when regex has capturing groups:
# REGEX_PATTERN = r"\[(.+)?\]\(((?:\/|https?:\/\/).+)\)"
#  without capturing groups re.findall() returns a list of correspondent strings:
REGEX_PATTERN_URL_MD_WRAPPED = r"\[(?:.+)?\]\((?:\/|https?:\/\/.+)\)"
REGEX_PATTERN_URL_PARENTHESIS_WRAPPED = r"\(((?:\/|https?:\/\/).+)\)"
REGEX_PATTERN_URL_NO_WRAP = r"(?:\/|https?:\/\/).+"

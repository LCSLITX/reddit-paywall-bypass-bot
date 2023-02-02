# the indentation is intentional. 
# The string should not use tabs to not broke markdown text when sent with request.
DYNAMIC_TEMPLATE = "Beep Beep. I'm a BOT who doesn't like Paywalls. 🤖 \n \
\n \
I do provide alternative links so you can read your news or articles without those annoying things. \n\
\n \
Here are your links: \
\n \
\n \
"
# the indentation is intentional. 
# The string should not use tabs to not broke markdown text when sent with request.
FIXED_TEMPLATE = "Beep Beep. I'm a BOT who doesn't like Paywalls. 🤖 \n \
\n \
I do provide links to news or articles without those annoying things. \n\
\n \
Here are your links in sequence: \
\n \
\n \
- {} \
\n \
\n \
- {} \
\n \
\n \
Beep beep. Bye."

FIRST_OPTION = "[First option](https://12ft.io/{})"
SECOND_OPTION = "[Second option](https://www.removepaywall.com/{})"

MULTI_FIRST_OPTION = "https://12ft.io/{}"
MULTI_SECOND_OPTION = "https://www.removepaywall.com/{}"

REGEX_PATTERN = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

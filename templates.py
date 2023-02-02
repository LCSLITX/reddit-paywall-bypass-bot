# the indentation is intentional. The string should not use tabs to not broke markdown text when sent with request.
dynamic_template = "Beep Beep. I'm a BOT who doesn't like Paywalls. 🤖 \n \
\n \
I do provide alternative links so you can read your news or articles without those annoying things. \n\
\n \
Here are your links: \
\n \
\n \
"
# the indentation is intentional. The string should not use tabs to not broke markdown text when sent with request.
fixed_template = "Beep Beep. I'm a BOT who doesn't like Paywalls. 🤖 \n \
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

first_option = "[First option](https://12ft.io/{})"
second_option = "[Second option](https://www.removepaywall.com/{})"

multi_first_option = "https://12ft.io/{}"
multi_second_option = "https://www.removepaywall.com/{}"

regex_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

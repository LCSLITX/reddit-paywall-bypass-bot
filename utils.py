import re
import templates


def regex_find(text):
  reg = re.findall(templates.regex_pattern, text)
  for index, elem in enumerate(reg):
    reg[index] = elem.rstrip(")")
  return reg


def build_reply_text(list):
  reply_text = templates.dynamic_template

  for index, url in enumerate(list):
    if index >= 3:
      break
    reply_text += f"{index + 1}º Link: [First Option]({templates.multi_first_option.format(url)}); [Second Option]({templates.multi_second_option.format(url)})  \n \
\n \
"
  reply_text += f"Beep beep. Bye."

  return reply_text
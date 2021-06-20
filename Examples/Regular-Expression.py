
import re

messages = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

name = phoneNumRegex.findall(messages)

print(name.group())



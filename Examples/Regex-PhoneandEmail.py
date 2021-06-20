#! python3

import re, pyperclip

# Create a regex for phone numbers
lyly = '''
((\d\d\d)|(\(\d\d\d)))?            # area code (optional)
(\s|-)            # first separator
\d\d\d            #first 3 digits
-            # separator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s)|x)            # extension word-part (optional)
(\d{2,5})?            # extension number-part (optional) 
'''
lyly = r'''
    (\d{3}|\(\d{3}\))?      # area code
    (\s|-|\.)?              # separator 
    (\d{3})                 # first 3 digits
    (\s|-|\.)               # separator
    (\d{4})                 # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
'''

phoneRegex = re.compile(lyly, re.VERBOSE | re.DOTALL)

# Create a regex for email addresses
emailRegex = re.compile(r'''
#some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9.+]+      # name part
@                   # @ symbol
[a-zA-Z0-9.+]+      # domain name part
''', re.VERBOSE | re.DOTALL)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractPhone = phoneRegex.findall(text)
extractEmail = emailRegex.findall(text)

print(extractPhone)
print(extractEmail)

# Copy the extracted email/phone to the clipboard

allPhoneNumbers = []
for phoneNumber in extractPhone :
    allPhoneNumbers.append(phoneNumber[0])
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractEmail)

pyperclip.copy(results)

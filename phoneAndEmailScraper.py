#! /usr/bin/env python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
#000-000-0000, 000-0000, (000) 000-0000, 000-0000 ext 0000, ext. 0000, x0000
(
((\d\d\d) | (\(\d\d\d\)))?        # area code (optional)
(\s|-)        # first seperator
\d\d\d        # first three digits
-        # seperator
\d\d\d\d        # last 4 digits
(((ext(\.)?\s)|x)        # extension word-part(optional)
(\d{2,5}))?      #extension number-part 
)
''',re.VERBOSE)



# Create a regex for email addresses
emailRegex = re.compile(r'''
#example.+_example@something.com

[a-zA-Z0-0_.+]+        # name part
@        # @ symbol
[a-zA-Z0-0_.+]+        # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email addresses and phone numbers from this text.
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

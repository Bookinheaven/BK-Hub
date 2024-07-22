"""
Task: Email Validator

Develop a Python function that validates whether a given string is a valid email
address. Implement checks for the format, including the presence of an "@" symbol and
a domain name
"""

from re import match

def isValidMail(mail):
    mailRegex = r'^[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}$'
    if match(mailRegex, mail):
        return True
    else:
        return False

testMails = [
    "test@example.com",
    "invalid-email.com",
    "another.test@domain.co",
    "invalid@yahoo.com",
    "user@libero.it",
    "user.name+tag+sorting@example.com",
    "@missingusername.com",
    "username@.com"
]

for mail in testMails:
    print(f"{mail}: {'Valid' if isValidMail(mail) else 'Invalid'}")

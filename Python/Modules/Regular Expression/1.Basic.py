import re


pattern = r'abc'
text = 'This is an abc example.'

# Search for the pattern
match = re.search(pattern, text)

if match:
    print("Pattern found!")
else:
    print("Pattern not found.")

pattern = r'\d+]'  # Matches one or more digits
text = 'There are 123 apples and 456 oranges.'

# Find all matches
matches = re.findall(pattern, text)

print("Matches found:", matches)

pattern = r'apples'
replacement = 'bananas'
text = 'I like apples. Apples are tasty.'

# Replace apples with bananas
new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

print("Replaced text:", new_text)

pattern = r'\s+'  # Matches one or more whitespace characters
text = 'Split this text into words.'

# Split the text
words = re.split(pattern, text)

print("Words:", words)

pattern = r'(\d+)\s+(\w+)'  # Matches digits followed by whitespace and words
text = '123 apples'

# Search for the pattern
match = re.search(pattern, text)

if match:
    number = match.group(1)  # First group (digits)
    word = match.group(2)    # Second group (word)
    print("Number:", number)
    print("Word:", word)

pattern = re.compile(r'\d+')

texts = ['123 apples', '456 oranges', '789 bananas']

for text in texts:
    match = pattern.search(text)
    if match:
        print(f"Match found in '{text}':", match.group())


pattern = r'^\d{3}$'  # Matches exactly three digits at the start and end of the string
text1 = '123'
text2 = '1234'

# Match patterns
match1 = re.match(pattern, text1)
match2 = re.match(pattern, text2)

print("Text1 match:", bool(match1))  # True
print("Text2 match:", bool(match2))  # False


pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
emails = ['test@example.com', 'invalid-email', 'user@domain.co']

for email in emails:
    match = re.match(pattern, email)
    if match:
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is NOT a valid email address.")

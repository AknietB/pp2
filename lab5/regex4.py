import re
def text_match(text):
    patterns='^[A-Z][a-z]+$'
    if re.search(patterns,text):
        return 'Found a match!'
    else:
        return 'Not matched!'
print(text_match("HELLO"))
print(text_match("Hello"))
print(text_match("HEllo"))
import re
def text_match(text):
    patterns='^a.b$'
    if re.search(patterns,text):
        return 'Found a match'
    else:
        return 'Not matched'
print(text_match("aCb"))
print(text_match("aba"))
print(text_match("Ab"))
print(text_match("ab"))

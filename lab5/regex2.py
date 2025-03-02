import re
def text_match(text):
    patterns='ab{2,3}?'
    if re.search(patterns,text):
        return 'Found a match!'
    else:
        return 'Not matched!'
print(text_match("bc"))
print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))
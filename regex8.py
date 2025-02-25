import re
def text_split(text):
    return re.findall(r'[A-Z][a-z]*',text)
print(text_split("HelloWorld")) 
print(text_split("PythonIsFun"))
print(text_split("SplitThisString")) 
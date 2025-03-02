import re
def text_replace(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print(text_replace("HelloWorld"))    
print(text_replace("PythonIsFun"))  
print(text_replace("InsertSpacesHere")) 

import re
def text_replace(text):
    return re.sub(r"[ ,.]",":",text)
print(text_replace("Hello, world. This is a test"))
print(text_replace("My name is Akniet, Im 17 years old."))
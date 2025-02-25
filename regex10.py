import re
def camel_to_snake(text):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()
print(camel_to_snake("helloWorld"))       
print(camel_to_snake("convertSnakeCase"))
print(camel_to_snake("pythonIsFun"))  

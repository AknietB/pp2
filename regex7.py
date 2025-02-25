import re
def snake_to_camel(text):
    components=text.split('_')
    return components[0]+''.join(word.capitalize() for word in components[1:])
print(snake_to_camel("hello_world"))   
print(snake_to_camel("convert_snake_case")) 
print(snake_to_camel("python_is_fun"))   
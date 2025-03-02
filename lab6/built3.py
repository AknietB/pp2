def palindrome(text):
    text=text.lower().replace(" ","")
    return text==text[::-1]
str=input()
if palindrome(str):
    print("Yes")
else:
    print("No")
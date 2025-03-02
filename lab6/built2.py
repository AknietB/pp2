def count_letter(str):
    upp=0
    low=0
    for a in str:
        if a.isupper():
            upp+=1
        else:
            low+=1
    return upp,low
s=input()
upper,lower=count_letter(s)
print(f"Uppercase: {upper}, Lowercase: {lower}")
def revers():
    a = input()
    words = a.split()
    reverse = reversed(words)
    sentence = ' '.join(reverse)
    return sentence
result = revers()
print(result)
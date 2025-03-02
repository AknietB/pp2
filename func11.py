def palin(s):
    s = s.lower() 
    s = s.replace(" ", "")  
    return s == s[::-1] 
a = input()
print("YES" if palin(a) else "NO")

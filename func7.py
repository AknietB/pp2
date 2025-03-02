def three(a):
    arr=[]
    for i in range(a):
        elem = int(input())
        arr.append(elem)
    for i in range(len(arr) - 1):
        if arr[i] == 3 and arr[i+1] == 3:
            return True
    return False
a = int(input())
if three(a):
    print("True")
else:
    print("False")
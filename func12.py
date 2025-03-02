def histogram():
    a = int(input())
    arr=[]
    for i in range(a):
        elem = int(input())
        arr.append(elem)
    for i in range(len(arr)):
        print("*" * arr[i])
histogram()
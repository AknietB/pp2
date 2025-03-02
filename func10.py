def unique():
    a = int(input())
    arr=[]
    arr2=[]
    for i in range(a):
        elem = int(input())
        arr.append(elem)
    for i in arr:
        if i not in arr2:
            arr2.append(i)
    print(arr2)
unique()
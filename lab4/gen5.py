def generator(N):
    for i in range(N,-1,-1):
        yield i
N=int(input())
for k in generator(N):
    print(k)
def generator(N):
    for i in range(0,N+1):
        if i%2==0:
            yield i

N=int(input())
for k in generator(N):
    print(k)
def generator_square(N):
    for i in range(1,N+1):
        yield i**2
N=int(input())
for k in generator_square(N):
    print(k)
class Prime():
    def __init__(self , n):
        self.n = n
    def list(self , arr):
        self.arr = arr
    def prime_filt(self , x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    def lam(self):
        print(list(filter(lambda x: self.prime_filt(x) , self.arr )))
n = int(input())
arr=[]
for i in range(n):
    a = int(input())
    arr.append(a)
answer = Prime(n)
answer.list(arr)
answer.lam()
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_prime():
    a = int(input())
    arr = []
    answer = []
    for i in range(a):
        elem = int(input())
        arr.append(elem)
    for i in arr:
        if is_prime(i):
            answer.append(i)
    print(answer)
filter_prime()
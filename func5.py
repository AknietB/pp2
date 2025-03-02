from itertools import permutations
def perm():
    s = str(input())
    answer = permutations(s)
    for i in answer:
        print(i)
perm()
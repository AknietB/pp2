def spy_game(nums):
    count = 0  
    for num in nums:
        if num == 0 and count == 0:  
            count = 1
        elif num == 0 and count == 1: 
            count = 2
        elif num == 7 and count == 2: 
            return True
    return False  
n = int(input())
arr = [int(input()) for _ in range(n)] 
if spy_game(arr):
    print("True")
else:
    print("False")

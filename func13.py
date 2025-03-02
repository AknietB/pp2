import random
def guess():
    print("Hello! What is your name?")
    name = str(input())
    print("Well, "+ name +", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    number = random.randint(1 , 20)
    a = int()
    count = 0
    while a!= number:
        count += 1
        a = int(input())
        if a < number:
            print("Your guess is too low")
            print("Take a guess.")
        elif a > number:
            print("Your guess is too great")
            print("Take a guess")
        else:
            print("Good job, " + name + "! You guessed my number in "+ str(count) +" guesses!")
guess()
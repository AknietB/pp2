import string
def files():
    for let in string.ascii_uppercase:
        with open(f"{let}.txt","w") as file:
            file.write(f"{let}.txt\n")
files()
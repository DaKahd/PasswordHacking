import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",\
 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
password = "c";
check = "incorrect"
def checkPassword():
     global check, guess
     while check == "incorrect":
        guess = ""
        guess = random.choice(alphabet)
        if guess == password:
            print("login correct")
            check = "correct"
    
while check != "correct":
    check = "incorrect"
    checkPassword()
    print(guess)


# SNAKE, WATER AND GUN GAME

import random

computer = random.choice(["s", "w", "g"])

user = input("Enter a choice (s, w, g): ")

print("You chose:", user)
print("Computer chose:", computer)

if computer == user:
    print("It's a Draw!")

elif computer == "w" and user == "s":
    print("You Win!")

elif computer == "g" and user == "w":
    print("You Win!")

elif computer == "s" and user == "g":
    print("You Win!")

else:
    print("Computer Wins!")


# THE PERFECT GUESS GAME

import random
num = random.randint(1,100)
a = -1
guesses = 1

while a != num:
    a = int(input("Guess the number :"))
    if a > num:
        print("lower number please")
        guesses +=1

    elif a < num:
        print("Higher number please")
        guesses +=1

print(f"You have guess the {num} correctly in {guesses} number ")

import random

num = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != num:
    if guess < num:
        print("your guess is too low. Better luck")
    elif guess > num:
        print("your guess is too High. Marvalus")

    guess = int(input("Guess again:"))
print("your guess is right")
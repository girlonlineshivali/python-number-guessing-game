import random

print("Welcome to my number guessing game! The computer has selected a number between 1 and 100 which you have to guess. Note: You can only enter numbers. Good luck!")
print()

number = random.randint(1, 100)
guess = int(input("Enter an integer from 1 to 100: "))
while number != "guess":
    if guess < number:
        print()
        print ("Your guess was too low.  Try again.")
        print()
        guess = int(input("Enter an integer from 1 to 100: "))
    elif guess > number:
        print()
        print ("Your guess was too high.  Try again.")
        print()
        guess = int(input("Enter an integer from 1 to 100: "))
    else:
        print()
        print ("Congrats! Your guess was correct. Play again by clicking the run button.")
        print()
        break


import random

number = random.randint(1, 9)
number_of_guesses = 0
while True:
    while True:
        try:
            guess = int(input("Guess a number between 1 and 9: "))
            if guess>=1 and guess<=9:
                break
            else:
                print("You must enter a number between 1 and 9, inclusive.")
        except ValueError:
            print("Enter a number!")
    number_of_guesses += 1
    if guess == number:            
        print(f"You took {number_of_guesses} guesses to guess the number {number}")
        break
    else:
        print("Incorrect")
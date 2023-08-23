import random
num=random.randint(1,9)
print("Guess my number, between 1 to 9. Type exit to exit.")
c=0
while True:
    guess=input("Guess: ")
    if guess=='exit':
        break
    else:
        guess=int(guess)
    if guess==num:
        print("You guessed correctly!")
        print(f"You took {c} incorrect guesses.")
        break
    elif guess>num:
        print("Too high")
        c+=1
    else:
        print("Too low")
        c+=1
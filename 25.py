import random
guesses=0
highest=100
lowest=0
print("I'll guess a number. Tell me if the guess is 'high' or 'low' or 'correct'.")
while True:
    g=random.randint(lowest, highest)
    print(f"Is it {g}?")
    guesses+=1
    user=input()
    if user=="high":
        highest=g-1
    elif user=="low":
        lowest=g+1
    elif user=="correct":
        print(f"Yay! It only took me {guesses} guesses!")
        break
    else:
        continue
def check(user, game, guesses, guessed):
    if user in guessed:
        guesses+=1
        return "Already tried"        
    elif user not in letters and user not in guessed:
        guessed.append(user)
        guesses+=1
        return "Incorrect!"
    else:
        guessed.append(user)
        guesses+=1
        game.replace("_",user)
        return game
    
word="EVAPORATE"
guesses=0
word=list(word)
guessed=set()
game=list("_"*len(word))
print(">>Welcome to Hangman!")
print(game)
print(word)
while True:
    user=input(">>Guess your letter: ").upper()
    
    if "_" not in game:
        print(str(game))
        print(f"Correct! You took {guesses} guesses.")
        break
    
    if user in guessed:
        print("Already tried!")
        print(f"You've guessed: {guessed}")
        guesses+=1
    
    elif user in word:
        index=word.index(user)
        game[index]=user
        word[index]="_"
        print("game", game)
def startgame():
    import random
    print("Welcome to the Cows and Bulls Game!")
    num=random.randint(1000, 9999)
    print("Enter a four digit number: ")
    guesses=0
    while True:
        cows, bulls=0, 0
        user=input(">>")
        if user=='exit':
            print("Number was",num)
            break
        guesses+=1
        l_num=list(str(num))
        l_user=list(user)      
        
        #print(l_num)
        
        for digit in l_num:
            if digit in l_user:
                bulls+=1
                if l_num.index(digit)==l_user.index(digit):
                    cows+=1
                    bulls-=1
                else:
                    pass
           
        if cows==4:
            print("Correct number! It was",num,". You took",guesses,"guesses.")
            break
        print(f"{cows} cows, {bulls} bulls. {guesses} so far.")
        cows, bulls=0, 0

if __name__=='__main__':
    startgame()
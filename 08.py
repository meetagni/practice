while True:
    s=input("Play again? Type 'no' to stop.\n")
    if s=='no':
        break
    else:
        p1=input("Player one, choose rock, paper or scissors: ")
        p2=input("Player two, choose rock, paper or scissors: ")
        if p1==p2:
            print("Draw")
        elif (p1=='rock' and p2=='scissors') or (p1=='paper' and p2=='rock') or (p1=='scissors' and p2=='paper'):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
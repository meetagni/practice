def drawboard(size):
    print(" ---"*size)
    for i in range(size):
        print("|",end='')
        print("   |"*size)
        print(" ---"*size)
        
size=int(input("Enter the size of board to draw: "))
drawboard(size)
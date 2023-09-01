game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

def print_game(game):
    print(game[0])
    print(game[1])
    print(game[2])

move_used=[]

def move(r,c,s):

    if [r,c] not in move_used: 
        move_used.append([r,c])
        game[r][c]=s
        print_game(game)            
    else:
        print("Move has already been used.")

print_game(game)
while True:    
    print("Player 1, enter 'row,column' for position of 'X'")
    p1=input(">>").split(',')
    r, c = int(p1[0])-1, int(p1[1])-1
    move(r,c,"X")

    print("Player 2, enter 'row,column' for position of 'O'")
    p2=input(">>").split(',')
    r, c = int(p2[0])-1, int(p2[1])-1
    move(r,c,"O")
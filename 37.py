#new way
def print_verticals(grid_size):
	vertical_string = "|"
	for i in range(grid_size):
		vertical_string += "   |"
	print(vertical_string)

def print_horizontals(grid_size):
	horiz_string = ""
	for i in range(grid_size):
		horiz_string += " ---"
	print(horiz_string)
 
grid_size_x = 3
grid_size_y = 5
print_horizontals(grid_size_x)
for i in range(grid_size_y):
	print_verticals(grid_size_x)
	print_horizontals(grid_size_x)

#modifying older way, from 24.py
def drawboard(x,y):
    print(" ---"*x)
    for i in range(y):
        print("|",end='')
        print("   |"*x)
        print(" ---"*x)
        
x=int(input("Enter the x of board to draw: "))
y=int(input("Enter the y of board to draw: "))
drawboard(x,y)
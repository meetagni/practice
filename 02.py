num=int(input("Give number:"))
check=int(input("Give check: "))
if num%4==0:
    print(f"{num} is multiple of 4")
elif num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

if num%check==0:
    print(f"{check} divides evenly into {num}")
else:
    print("Can't divide")
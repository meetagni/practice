a=int(input("first num: "))
b=int(input("second num: "))
c=int(input("third num: "))
largest=a
if b>largest:
    largest=b
if c>largest:
    largest=c
print(f"largest is {largest}")
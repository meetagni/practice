import datetime

name=input("Enter your name: ")
age=int(input("Enter your age: "))

current_year= datetime.datetime.now().year

y=current_year-age+100
print(f"{name}'ll be 100 in the year {y}")
def prime(num):
    factors=0
    for n in range(1,num+1):
        if num%n==0:
            factors+=1
    if factors<=2:
        return f"{num} is prime."
    else:
        return f"{num} is composite."

num=int(input("Enter a number to check: "))
print(prime(num))
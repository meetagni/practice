num=int(input("Give number: "))
l=range(1,num)
print([i for i in l if num%i==0])
def fib(l):
    if l<=0:
        return "Invalid"
    elif l==1:
        return "1"
    else:
        seq=[1,1]
        for i in range(l-2):
            seq.append(seq[i]+seq[i+1])
        return seq

l=int(input("How many fibonacci numbers?\n"))
print(fib(l))
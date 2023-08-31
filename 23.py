primenumbers=[]
with open("primenumbers.txt","r") as pn:
    line=pn.readline()
    while line:
        primenumbers.append(int(line))
        line=pn.readline()
print("total prime numbers=",len(primenumbers))

happynumbers=[]
with open("happynumbers.txt","r") as hn:
    line=hn.readline()
    while line:
        happynumbers.append(int(line))
        line=hn.readline()
print("total happy numbers=",len(happynumbers))

overlapping=[elem for elem in primenumbers if elem in happynumbers]
print("total overlapping numbers=",len(overlapping))
print("the numbers are",overlapping)
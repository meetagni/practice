dik=dict()
with open("nameslist.txt", "r") as f:
    line=f.readline()
    while line:
        line=line.strip()
        if line in dik:
            dik[line]+=1
        else:
            dik[line]=1
        line=f.readline()
        
print(dik)

dic2=dict()
with open("Training_01.txt", 'r') as f2:
    line=f2.readline()
    while line:
        line=line.strip()
        line=line[3:-26]
        if line in dic2:
            dic2[line]+=1
        else:
            dic2[line]=1
        line=f2.readline()

print(dic2)
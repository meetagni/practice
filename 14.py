def make_set(l):
    return set(l)

def using_loop(l):
    y=[]
    for i in l:
        if i not in y:
            y.append(i)
    return y

def enter_list():
    l=[]
    while True:
        i=input("Enter number: ")
        if i=='':
            break
        else:
            l.append(int(i))
    return l

l=enter_list()
print(make_set(l))
print(using_loop(l))
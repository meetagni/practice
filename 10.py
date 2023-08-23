import random
a = random.sample(range(1,30), 11)
b = random.sample(range(1,30), 12)
c = [element for element in a if element in b]
d = [i for i in c if c.count(i)==1]
print('a=', a)
print('b=', b)
print(c)
print(d)
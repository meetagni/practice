def reverse(s):
    l1=s.split()
    l2=l1[::-1]
    s2=' '.join(l2)
    return s2

s1=input("Enter a sentence: ")
print(s1,"\nNow the reversed:")
print(reverse(s1))
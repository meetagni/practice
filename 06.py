s1=input("Enter a string: ")
s2=s1[-1::-1]
print(s1)
print(s2)
if s1==s2:
    print("Palindrome")
else:
    print("Not a palindrome")
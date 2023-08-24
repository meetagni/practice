import random
def psswrd(length, strength):
    if strength=="weak":
        s="abcdefghijklmnopqrstuvwxyz"
        return "".join(random.sample(s,length))
    elif strength=="strong":
        s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        return "".join(random.sample(s,length))
    else:
        return "invalid"

length=int(input("Enter a password length: "))
strength=input("weak or strong?: ")
new_pass=psswrd(length, strength)
print(f"New password: {new_pass}")
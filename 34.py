import json
# info_about_me={
#     "name":"Michele",
#     "has_a_dog":False
# }
# with open("info.json","w") as f:
#     json.dump(info_about_me, f)
    
# with open("info.json","r") as f:
#     info=json.load(f)

# #print(info)
    
# if info["has_a_dog"]:
#     print("{} has a dog".format(info["name"]))
# else:
#     print("{} does not have a dog".format(info["name"]))

def add(name):
    print("Name is",name)
    print("What is their birth date?")
    date=input()
    new={name:date}
    birthdays.update(new)
    with open("birthdays.json", "w") as f:
        json.dump(birthdays, f)
 
birthdays={}
with open("birthdays.json","r") as f:
    birthdays=json.load(f)
    
print("We have birthdays of:")
for key in birthdays:
    print(key)
name=input("\nWhose birthday do you wish to see?\n")
if name in birthdays:
    print(birthdays[name])
else:
    print("Not found. Do you wish to add? y/n")
    user=input()
    if user=='y':
        add(name)
        print("Added.")
    elif user=='n':
        print("Nothing added.")
    else:
        print("invalid")
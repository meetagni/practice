from collections import Counter
import json
num_to_month={"01":"Jan",
              "02":"Feb",
              "03":"Mar",
              "04":"Apr",
              "05":"May",
              "06":"Jun",
              "07":"Jul",
              "08":"Aug",
              "09":"Sep",
              "10":"Oct",
              "11":"Nov",
              "12":"Dec"
              }

birthdays={}

with open("birthdays.json","r") as f:
    birthdays=json.load(f)

dates=list(birthdays.values())
months=[]
for date in dates:
    months.append(date[:2])

new_l=[]
for month in months:
    new_l.append(num_to_month[month])
    
c=Counter(new_l)
print(c)
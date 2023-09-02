from bokeh.plotting import figure, show, output_file
import json
from collections import Counter

output_file("plot.html")

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

def bdays(birthdays, num_to_month):

    dates=list(birthdays.values())
    months=[]
    for date in dates:
        months.append(date[:2])

    new_l=[]
    for month in months:
        new_l.append(num_to_month[month])
        
    c=Counter(new_l)
    return c
    
birthdays={}
with open("birthdays.json","r") as f:
    birthdays=json.load(f)

x_categories=list(num_to_month.values())
c=bdays(birthdays, num_to_month)
x=list(c.keys())
y=list(c.values())
p=figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)
show(p)
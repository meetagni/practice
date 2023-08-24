import requests
from bs4 import BeautifulSoup

url='https://www.nytimes.com'
r=requests.get(url)
r_html=r.text
# soup=BeautifulSoup(r_html, features="html.parser")

# for story_heading in soup.find_all(class_="story-heading"):
#     if story_heading.a:
#         print(story_heading.a.text.replace("\n"," ").strip())
#     else:
#         print(story_heading.contents[0].strip())

print(r.encoding)
soup = BeautifulSoup(r_html, 'html.parser')
title = soup.find('title').text
print(title, "\n")

for heading in soup.find_all(class_="css-4m8aqz e1lsht870"):
    if heading.a:
        pass
# print(heading.a.text)
    else:
        print(heading.contents[0])

print("\n \n")

for heading in soup.find_all(class_="css-13shibb"):
    if heading.a:
        pass
# print("\n", heading.a.text)
    else:
        print(heading.contents[0].text)
import requests
from bs4 import BeautifulSoup

page= requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup= BeautifulSoup(page.content, 'html.parser')

first_h1= soup.select('h1')[0].text 

print(first_h1)  


#-------------------------------------------------
all_h1_tags= []
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

seventh_p_text= soup.select('p')[6].text 

print(all_h1_tags, seventh_p_text) 
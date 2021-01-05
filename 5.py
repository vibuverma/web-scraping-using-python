## Extracting all the text information from the site

import requests 
from bs4 import BeautifulSoup 

# Create top_items as empty list
top_items= []

page= requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup= BeautifulSoup(page.content, 'html.parser')

products= soup.select('div.thumbnail')

for element in products:
    title= element.select('h4 > a.title')[0].text 
    review_lable= element.select('div.ratings')[0].text 
    info= {
        'title': title.strip(),
        'review': review_lable.strip()
    }
    top_items.append(info)

print(top_items)  

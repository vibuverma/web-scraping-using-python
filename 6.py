## Extracting Links from the WebSite

import requests
from bs4 import BeautifulSoup

page= requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup= BeautifulSoup(page.content, 'html.parser')

# Creating image_data as empty list
image_data= []

# Extracting image links
images= soup.select('img')
for image in images:
    src= image.get('src')
    alt= image.get('alt')
    image_data.append({"src":src, "alt":alt})

#print(image_data) 

#------------------------------------------------------------------------

all_links= []
links= soup.select('a')
for aherf in links:
    text= aherf.text 
    text= text.strip() if text is not None else ' '

    href= aherf.get('href')
    href= href.strip() if href is not None else ' '

    all_links.append({"href": href, "text":text})

print(all_links)
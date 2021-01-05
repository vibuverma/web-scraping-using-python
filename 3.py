import requests
from bs4 import BeautifulSoup

page= requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup= BeautifulSoup(page.content, "html.parser")

#Extracting Title
page_title= soup.title

#Extracting head
page_head= soup.head.text 

print(page_head) 
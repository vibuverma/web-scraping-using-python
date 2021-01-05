import requests




res= requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')
txt= res.text
status= requests.status_codes

print(txt)
print(status)

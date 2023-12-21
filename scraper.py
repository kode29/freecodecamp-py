import requests
from bs4 import BeautifulSoup

url = "https://kylemperkins.com"
r = requests.get(url)
    
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find_all('div', {'class': 'skill-item'})

# Print all items found, ignore HTML tags
for skill in title:
    print(skill.getText())

# Print all "skills" (nested inside the above class)c
for skillItem in title:
    skill = skillItem.find("h5")
    print(skill.getText())
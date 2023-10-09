import requests
from bs4 import BeautifulSoup

params = {
    'lang': 'in',
    'mod': 'latest_jobs',
    'num': '1',
}

burl = 'https://jobindo.com/'
response = requests.get('https://jobindo.com/index.php', params=params)
print(response)

soup = BeautifulSoup(response.text, "lxml")
print(soup.title)

h1 = soup.find(attrs={"class": "results-job-title-link"})
print(h1.string)

a_href=soup.findAll("a",{"class":"results-job-title-link"})
lis = []
for lk in a_href:
    # link = burl+a_href['href'].text
    link = lk['href']
    l = burl+link
    lis.append(l)

print(lis)

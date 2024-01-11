import re
import requests
from bs4 import BeautifulSoup
from lxml import etree

key = input('Masukan kata kunci :')

def get_pg(pg):
    param = [
        ('mod', 'search'),
        ('job_title', key),
        ('lang', 'in'),
        ('sort', 'asc'),
        ('num', str(pg)),
    ]
    # print(param)
    return param


def get_count(param):
    response = requests.get('https://jobindo.com/index.php', params=param)
    print(response)
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup.title)
    # h1 = soup.find(attrs={"class": "results-job-title-link"})
    # print(h1.string)
    h2 = soup.find('h2', class_='no-margin')
    h2 = str(h2.text)
    numbers = re.findall(r'\d+', h2)
    h2 = int(numbers[0])
    print('jumlah jobs :', h2)
    pgjob = int(h2)
    mjob = pgjob % 20
    pg = pgjob // 20
    if mjob > 0:
        pg += 1    
    print('jumlah page :', pg)    

def get_joblist(param):
    response = requests.get('https://jobindo.com/index.php', params=param)
    burl = 'https://jobindo.com/'
    # print(response)
    soup = BeautifulSoup(response.text, "lxml")
    a_href=soup.findAll('a', class_='results-job-title-link')
    
    
    soup1 = BeautifulSoup(response.content, 'html.parser')
    body = soup1.find("body")    
    lis = []
    i=1
    for lk in a_href:
        # link = burl+a_href['href'].text
        link = lk['href']
        l = burl+link
        # print(l)
        i +=1
        a = i % 2
        if a == 0:
            lis.append(l)
    # print(lis)  
    return lis

def get_detail(a):
    res = requests.get(a)
    soup = BeautifulSoup(res.text, "lxml")
    pos = soup.find('h1', class_='no-margin h1title-job')
    posisi = pos.string
    return posisi
    
    
if __name__=='__main__':
    param = get_pg(1)
    get_count(param)
    pg = int(input('Masukan jumlah page :'))
    all_lis = []
    for i in range(1, pg+1):
        param = get_pg(i)
        # print(param)
        lis = get_joblist(param)
        all_lis.extend(lis)
    print(all_lis)
    i=1
    for a in all_lis:
        print(i)
        print(a)
        # posisi = get_detail(a)
        # print(posisi)
        i +=1

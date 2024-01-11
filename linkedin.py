import requests
from bs4 import BeautifulSoup
from datetime import datetime

cari = input('Masukan Key : ',)

response = requests.get(
f'https://www.linkedin.com/jobs/search?keywords={cari}&location=Indonesia&locationId=&geoId=102478259&f_TPR=&f_PP=102157348%2C102471123%2C105898461&f_WT=1&f_JT=F%2CC&position=1&pageNum=0')

#print(response)
soup = BeautifulSoup(response.text, "lxml")
#print(soup.title)

print('-----------------------------------------')  
ddd = soup.find('div', class_='base-serp-page__content')
#print(ddd)
ulul = ddd.find('ul')
#print(ulul)

url = ulul.findAll('a', class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')
#print(len(url))

posisi = ulul.findAll('span', class_='sr-only')
#print(len(posisi))

nama = ulul.findAll('a', class_='hidden-nested-link')
#print(len(nama))

lokasi = ulul.findAll('span', class_='job-search-card__location')
#print(len(lokasi))

pdate = ulul.findAll('time', class_='job-search-card__listdate')
#print(len(pdate))

jlm = len(posisi)
i=0
jobrow = 0
for e in range(0, jlm):
    pst = posisi[i].text
    pst = pst.strip()
    lk = url[i]
    nm = nama[i].string
    nm = nm.strip()
    lok = lokasi[i].string
    lok = lok.strip()
    try:
        dtt = pdate[i]
        dtt = dtt['datetime']
        dt = pdate[i].string
        dt = dt.strip()
    except:
        dt = ''
        dtt = ''
    lkn = lk['href']
    slk = lkn.split('?')
    print(i+1)
    print('Posisi   : ',pst)
    print('Nama     : ',nm)
    print('Alamat   : ',lok)
    print('Link     : ',str(slk[0]))
    print('Date     : ',dt, '(',dtt,')')
    i += 1
    print('-------------------------------------------------------------------')
    jobrow += 1
    if jobrow >= 5:
        ln = input('Tampilkan 5 job lagi... (y/n)')
        if ln == 'n':
            break
        else:
            print('==================================')
            jobrow = 0

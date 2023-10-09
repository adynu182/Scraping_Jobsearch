import requests
from requests_html import HTMLSession

def get_page(pg):
    url = f"https://www.loker.id/cari-lowongan-kerja/page/{pg}?q&lokasi=banten&category=administrasi&pendidikan=0"
    try:
        s = HTMLSession()
        r = s.get(url)
        # isi = r.text
        # print(r)
    except requests.exceptions.RequestException as e:
        print(e)
    return r  

def get_pg():
    r = get_page(1)
    page = r.html.find('div.container.m-t-20 > div.m-b-40 > div.row.pagination-bar.margin-top-1em > div.col-md-5 > div > strong')
    pg = int(page[2].text)
    return pg
    
def get_jobs(jm):
    lis = []
    for i in range(1, jm+1):
        r = get_page(i)
        # posisi = r.html.find('div.col-md-3 > div > div.media-body > h2')
        # pt = r.html.find('div.col-md-4 > table')
        # for posisi in posisi:
            # posisi = posisi.text
            # print(posisi)
        # for pt in pt:    
            # pt = pt.text
            # pt = pt.split('\n')
            # n = 0
            # for i in range(1,4):
                # pt.pop(n)
                # n += 1   
            # print(pt) 
        sumber = r.html.find('div.col-xs-12.col-sm-12.col-md-2.col-md-offset-8.col-action.m-b-5')
        for item in sumber:   
            link = item.find('a', first=True).attrs['href']
            # print(link)
            lis.append(link)
    for lis in lis:
        try:
            s = HTMLSession()
            r = s.get(lis)
            # isi = r.text
            # print(r)
        except requests.exceptions.RequestException as e:
            print(e)
        nama = r.html.find('div.panel-heading.padding-horizontal-double')
        # deskrip = 
        dtl = []
        for nama in nama:
            # print(nama.text)
            nama = nama.text
            # print('---------------------------------')
            dtl.append(nama)
        dtl.pop()
        dtl.pop()
        dtl.pop()
        print(dtl)
        

      
if __name__ =='__main__' :    
    jlmpg = get_pg()
    print(jlmpg)
    js = jlmpg % 9
    jm = jlmpg // 9
    if js > 0 : jm +=1 
    print(jm)
    jm = int(input('masukan jumlah page yang akan di scrape : '))
    get_jobs(jm)
        

#primary > div > div > div > div.col-md-8 > div > div > div:nth-child(2) > div.panel-body.padding-horizontal-double.padding-vertical-double
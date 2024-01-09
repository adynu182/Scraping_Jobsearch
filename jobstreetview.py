import requests

cari = input('Masukan Kata Kunci : ')

joblok = ['Banten','Jakarta Raya']

headers = {
    'authority': 'www.jobstreet.co.id',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.jobstreet.co.id/id/admin-jobs',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'seek-request-brand': 'jobstreet',
    'seek-request-country': 'ID',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-seek-site': 'Chalice',
}

params = {
    'siteKey': 'ID-Main',
    'sourcesystem': 'houston',
    'where': joblok[0],
    'page': '1',
    'seekSelectAllPages': 'true',
    'keywords': cari,
    'sortmode': 'ListedDate',
    'pageSize': '30',
    'include': 'seodata',
    'locale': 'id-ID',
}

requ = requests.get('https://www.jobstreet.co.id/api/chalice-search/v4/search', params=params, headers=headers).json()

print('Total Jobs   : ',requ['totalCount'])
print('Total Page   : ',requ['totalPages'])
print('-------------------------------')

pg = int(requ['totalPages'])

def get_total(pg):
    par = []
    for e in range (pg):
        params = {
        'siteKey': 'ID-Main',
        'sourcesystem': 'houston',
        'where': joblok[0],
        'page': str(e+1),
        'seekSelectAllPages': 'true',
        'keywords': cari,
        'sortmode': 'ListedDate',
        'pageSize': '30',
        'include': 'seodata',
        'locale': 'id-ID',
        }
        par.append(params)
    return par

def get_detail(params):  
    dt = []
    req = requests.get('https://www.jobstreet.co.id/api/chalice-search/v4/search', params=params, headers=headers).json()
    rows = req['data']
    base = 'https://www.jobstreet.co.id/id/job/'
    jobrow = 0
    for i in range (len(rows)):
        id = rows[i]['id']
        #id = rows[i]['solMetadata']['jobId']
        nama = rows[i]['advertiser']['description']
        bidang = rows[i]['title']
        tipe = rows[i]['workType']
        lokasi = rows[i]['jobLocation']['label']
        pdate = rows[i]['listingDateDisplay']
        gaji = rows[i]['salary']
        if gaji == None:
            gaji = '-'
        divisi = rows[i]['classification']['description']
        
        print(i+1, id, '(Date : ',pdate,')')
        try:
            print('Posisi   : ',bidang)
        except:
            print(bidang.encode())
        
        print('Kategori : ',divisi)
        print('Lokasi   : ',lokasi)
        print('Nama     : ',nama)
        print('Type     : ',tipe)
        print('Gaji     : ',gaji)
        #print('Posted   : ',pdate)
        print('Link     : ',base+str(id))
        print('--------------------------------------------------------')
  
        jobrow += 1
        if jobrow >= 4:
            ln = input(f'Tampilkan 4 lagi... (y/n)')
            if ln == 'n':
                return ln
            else:
                print('==================================================================')
                jobrow = 0
                
if __name__ == '__main__':
    jobpage = 0
    par = get_total(pg)
    data_all = []
    for w in range (len(par)):
        ln = get_detail(par[w])
        jobpage += 1
        if jobpage >= 1:
            if ln == 'n':
                break
            else:
                print('==== Next Page =======')
                jobpage = 0

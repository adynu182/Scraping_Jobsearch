import requests

headers = {
    'authority': 'www.kalibrr.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
def get_pg(pg,pos):
    pos = pos.replace(" ","+")
    url = f'https://www.kalibrr.com/kjs/job_board/search?limit={pg}&offset=0&text={pos}&location=Dki+Jakarta,Tangerang&sort_direction=desc&sort_field=activation_date'
    r = requests.get(url, headers=headers)
    # print(r)
    # print(url)
    res = r.json()
    
    return res

def get_jobs(res):
    jlm = res['count']
    print(jlm)
    rows = res['jobs']
    lim = 0
    for i in range(0, len(rows)):
        if lim >= 5:
            ln = input(f'Jlm ({jlm}) Tampilkan 5 job lagi... (y/n)')
            if ln == 'n':
                return
            else:
                print('==================================')
                lim = 0
        lim +=1            
        print(i)
        print('Perusahaan : ',rows[i]['company_name'])
        print('Posisi     : ',rows[i]['name'])
        pdate = rows[i]['activation_date']
        edate = rows[i]['application_end_date']
        industri = rows[i]['company']['industry']
        try:
            lok = rows[i]['google_location']['address_components']['city']  
        except:
            lok = ''
        link = rows[i]['company_info']['code']
        link2 = rows[i]['id']
        link3 = rows[i]['slug']
        
        print('Industri   : ',industri)
        print('post date  : ',pdate[0:10])
        print('end date   : ',edate[0:10])
        print('Lokasi     : ',lok)
        print(f"Link       :  https://www.kalibrr.com/c/{link}/jobs/{link2}/{link3}")
        print('---------------------------------------')
        
        
        
    
if __name__=='__main__':
    pos = input('masukan kata kunci : ')
    res = get_pg(15, pos)
    print('jumlah loker : ',res['count'])
    pg = res['count']
    res = get_pg(pg,pos)
    get_jobs(res)
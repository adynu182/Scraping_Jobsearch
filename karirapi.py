import requests
url = 'https://www.karir.com'
def get_tot(q,pg):
    params = {
        'q': q,
        'sort_order': 'newest',
        'job_function_ids': '',
        'industry_ids': '',
        'degree_ids': '',
        'major_ids': '',
        'location_ids': '',
        'location_id': '',
        'location': '',
        'salary_lower': '0',
        'salary_upper': '100000000',
        'page': str(pg),
        'grid': 'list',
    }
    return params

def get_job(q,pg):
    # paraml = get_param(a,b)
    # for param in paraml:
    no = 1
    jobrow = 0
    for u in range(1,pg+1):  
        params = {
            'q': q,
            'sort_order': 'newest',
            'job_function_ids': '',
            'industry_ids': '',
            'degree_ids': '',
            'major_ids': '',
            'location_ids': '',
            'location_id': '',
            'location': '',
            'salary_lower': '0',
            'salary_upper': '100000000',
            'page': str(u),
            'grid': 'list',
        }
        res = requests.get('https://www.karir.com/search.json', params=params).json()
        rows = res['collection']
                
        for i in range(0, len(rows)):
            nama = rows[i]['company']['billing_company_name']
            link = rows[i]['show_path']
            age = rows[i]['required_max_age']
            jobs = rows[i]['job_position']
            date = rows[i]['posted_at_formatted']
            loc = rows[i]['location']['name']
            # requ = rows[i]['requirements']
            # r = requ.replace("<p>","")
            # r = r.replace("</p>","")
            # r = r.replace("<ul>","")
            # r = r.replace("</ul>","")
            # r = r.replace("<li>","")
            # r = r.replace("</li>","")
            # r = r.replace("<br>","")
            # r = r.strip()
            # r = r.strip("  ")
            if age >= 35:
                print(no)
                no += 1
                print('Posisi     :', jobs)
                print('Perusahaan :', nama)
                links = url+link
                print('Link       :', links)
                print('Umur       :', age ,'Tahun')
                print('Lokasi     :', loc)
                print('Post Date  :', date)
                # print(r)
                print('---------------------------------')
                jobrow += 1
                if jobrow >= 5:
                    ln = input(f'Jlm ({pg}) Tampilkan 5 job lagi... (y/n)')
                    if ln == 'n':
                        return
                    else:
                        print('==================================')
                        jobrow = 0
                  
if __name__=='__main__':
    q = input('Masukan Kata kunci : ')
    par = get_tot(q,1)
    res = requests.get('https://www.karir.com/search.json', params=par).json()
    pg = res['pagination_size']
    print('Total Page :', pg)
    print('-------------------------------------------')
    get_job(q,pg)

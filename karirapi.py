import requests


params = {
    'q': 'admin',
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
    'page': '4',
    'grid': 'list',
}

res = requests.get('https://www.karir.com/search.json', params=params).json()
url = 'https://www.karir.com'

rows = res['collection']
for i in range(0, len(rows)):
    nama = rows[i]['company']['billing_company_name']
    link = rows[i]['show_path']
    age = rows[i]['required_max_age']
    print(nama)
    links = url+link
    print(links)
    print(age)
    

import requests
import re

cari = input('Masukan Kata Kunci : ')

headers= {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Cache-Control' : 'no-cache'
        }
        
json_data = {
    'operationName': 'searchJobs',
    'variables': {
        'data': {
            'SearchTerm': cari,
            'CountryCode': 'ID',
            'sortBy': 'LATEST',
            'LocationIds': [
                'ea61f4ac-5864-4b2b-a2c8-aa744a2aafea',
                '3d6ac5e8-f12d-40cd-823d-44597402ea3b',
                '078b37b2-e791-4739-958e-c29192e5df3e',
                'e2a615bb-0997-42c8-a018-c4a1768ae01f',
                'af0ed74f-1b51-43cf-a14c-459996e39105',
                '262b7d3c-2c51-4854-a7e8-6635e0657338',
                'fbc373c5-cadc-4dd8-acb3-1e57850e2a08',
                'f5817918-7ce1-436d-9478-c438b3466adb',
                '87c39cfb-0e3c-4edb-a7a0-754fb70cc587',
                '826664b3-1f31-497f-bc8a-a23699b1a531',
                '337f8da8-70d8-4916-9733-1cee8e4902e9',
                'ae3c458e-5947-4833-8f1b-e001ce2fad1d',
                'd305a80e-4891-45a4-8c5b-29c9242f431e',
            ],
            'limit': 30,
            'offset': 0,
            'includeExternalJobs': True,
            'sources': [
                'NATIVE',
                'SUPER_POWERED',
            ],
            'searchVariant': 'VARIANT_A',
        },
    },
    'query': 'query searchJobs($data: JobSearchConditionInput!) {\n  searchJobs(data: $data) {\n    jobsInPage {\n      id\n      title\n      isRemote\n      status\n      createdAt\n      updatedAt\n      isActivelyHiring\n      isHot\n      shouldShowSalary\n      educationLevel\n      type\n      salaryEstimate {\n        minAmount\n        maxAmount\n        CurrencyCode\n        __typename\n      }\n      company {\n        ...CompanyFields\n        __typename\n      }\n      citySubDivision {\n        id\n        name\n        __typename\n      }\n      city {\n        ...CityFields\n        __typename\n      }\n      country {\n        ...CountryFields\n        __typename\n      }\n      category {\n        id\n        name\n        __typename\n      }\n      salaries {\n        ...SalaryFields\n        __typename\n      }\n      location {\n        ...LocationFields\n        __typename\n      }\n      minYearsOfExperience\n      maxYearsOfExperience\n      source\n      type\n      hierarchicalJobCategory {\n        id\n        level\n        name\n        children {\n          name\n          level\n          id\n          __typename\n        }\n        parents {\n          id\n          level\n          name\n          __typename\n        }\n        __typename\n      }\n      skills {\n        skill {\n          id\n          name\n          __typename\n        }\n        mustHave\n        __typename\n      }\n      __typename\n    }\n    numberOfJobsCreatedInLast14Days\n    totalJobs\n    __typename\n  }\n}\n\nfragment CompanyFields on Company {\n  id\n  name\n  logo\n  status\n  __typename\n}\n\nfragment CityFields on City {\n  id\n  name\n  __typename\n}\n\nfragment CountryFields on Country {\n  code\n  name\n  __typename\n}\n\nfragment SalaryFields on JobSalary {\n  id\n  salaryType\n  salaryMode\n  maxAmount\n  minAmount\n  CurrencyCode\n  __typename\n}\n\nfragment LocationFields on HierarchicalLocation {\n  id\n  name\n  administrativeLevelName\n  formattedName\n  level\n  slug\n  parents {\n    id\n    name\n    administrativeLevelName\n    formattedName\n    level\n    slug\n    parents {\n      level\n      formattedName\n      slug\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n',
}

base_url = 'https://glints.com/id/opportunities/jobs/'
res = requests.post('https://glints.com/api/graphql', headers=headers, json=json_data)

print(res)
response = res.json()

total = response['data']['searchJobs']['totalJobs']
rows = response['data']['searchJobs']['jobsInPage']

i = 0
jobrow = 0
#jobs = []
# for i in range(0, len(rows)):
for row in rows:
    nama = row['title']
    parse = nama.split(' ')
    domain = '-'.join(parse)
    domain = domain.lower()
        
    perusahaan = row['company']['name']
    lokasi = row['city']['name']
    published = row['updatedAt']
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    date_post = re.search(date_pattern,published)
    link = base_url + domain+ '/'+ row['id']
    
    skills = row['skills']
    keterampilan =[]
    for skill in skills:
        sklname = skill['skill']['name']
        keterampilan.append(sklname)
        
    i+=1
    #jobs.append(
    #    (nama, perusahaan, lokasi, date_post[0], keterampilan, link)
    #)
    print(i)
    print('Post Date    : ',date_post[0])
    try:
        print('Posisi       : ',nama)
    except:
        print(nama.encode())
    try:
        print('Perusahaan   : ',perusahaan)
    except:
        print(perusahaan.encode())
    print('Alamat       : ',lokasi)
    print('Skill        : ',keterampilan)
    try:
        print('Url          : ',link)
    except:
        print(link.encode())
    print('--------------------------------------------')
    jobrow += 1
    if jobrow >= 5:
        ln = input(f'Jlm ({total}) Tampilkan 5 job lagi... (y/n)')
        if ln == 'n':
            break
        else:
            print('==================================')
            jobrow = 0

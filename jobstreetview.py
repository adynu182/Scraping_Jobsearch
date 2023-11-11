import requests
import pandas as pd
import time
import sys, os
import re

cari = input('Masukan Kata Kunci : ')


headers = {
    'authority': 'xapi.supercharge-srp.co',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'origin': 'https://www.jobstreet.co.id',
    'referer': 'https://www.jobstreet.co.id/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

params = {
    'country': 'id',
    'isSmartSearch': 'true',
}

json_data = {
    'query': 'query getJobs($country: String, $locale: String, $keyword: String, $createdAt: String, $jobFunctions: [Int], $categories: [String], $locations: [Int], $careerLevels: [Int], $minSalary: Int, $maxSalary: Int, $salaryType: Int, $candidateSalary: Int, $candidateSalaryCurrency: String, $datePosted: Int, $jobTypes: [Int], $workTypes: [String], $industries: [Int], $page: Int, $pageSize: Int, $companyId: String, $advertiserId: String, $userAgent: String, $accNums: Int, $subAccount: Int, $minEdu: Int, $maxEdu: Int, $edus: [Int], $minExp: Int, $maxExp: Int, $seo: String, $searchFields: String, $candidateId: ID, $isDesktop: Boolean, $isCompanySearch: Boolean, $sort: String, $sVi: String, $duplicates: String, $flight: String, $solVisitorId: String) {\n  jobs(\n    country: $country\n    locale: $locale\n    keyword: $keyword\n    createdAt: $createdAt\n    jobFunctions: $jobFunctions\n    categories: $categories\n    locations: $locations\n    careerLevels: $careerLevels\n    minSalary: $minSalary\n    maxSalary: $maxSalary\n    salaryType: $salaryType\n    candidateSalary: $candidateSalary\n    candidateSalaryCurrency: $candidateSalaryCurrency\n    datePosted: $datePosted\n    jobTypes: $jobTypes\n    workTypes: $workTypes\n    industries: $industries\n    page: $page\n    pageSize: $pageSize\n    companyId: $companyId\n    advertiserId: $advertiserId\n    userAgent: $userAgent\n    accNums: $accNums\n    subAccount: $subAccount\n    minEdu: $minEdu\n    edus: $edus\n    maxEdu: $maxEdu\n    minExp: $minExp\n    maxExp: $maxExp\n    seo: $seo\n    searchFields: $searchFields\n    candidateId: $candidateId\n    isDesktop: $isDesktop\n    isCompanySearch: $isCompanySearch\n    sort: $sort\n    sVi: $sVi\n    duplicates: $duplicates\n    flight: $flight\n    solVisitorId: $solVisitorId\n  ) {\n    total\n    totalJobs\n    relatedSearchKeywords {\n      keywords\n      type\n      totalJobs\n    }\n    solMetadata\n    suggestedEmployer {\n      name\n      totalJobs\n    }\n    queryParameters {\n      key\n      searchFields\n      pageSize\n    }\n    experiments {\n      flight\n    }\n    jobs {\n      id\n      adType\n      sourceCountryCode\n      isStandout\n      companyMeta {\n        id\n        advertiserId\n        isPrivate\n        name\n        logoUrl\n        slug\n      }\n      jobTitle\n      jobUrl\n      jobTitleSlug\n      description\n      employmentTypes {\n        code\n        name\n      }\n      sellingPoints\n      locations {\n        code\n        name\n        slug\n        children {\n          code\n          name\n          slug\n        }\n      }\n      categories {\n        code\n        name\n        children {\n          code\n          name\n        }\n      }\n      postingDuration\n      postedAt\n      salaryRange {\n        currency\n        max\n        min\n        period\n        term\n      }\n      salaryVisible\n      bannerUrl\n      isClassified\n      solMetadata\n    }\n  }\n}\n',
    'variables': {
        'keyword': cari,
        'jobFunctions': [],
        'locations': [
            32900,
            30501,
        ],
        'salaryType': 1,
        'jobTypes': [],
        'createdAt': None,
        'careerLevels': [],
        'page': 1,
        'sort': 'createdAt',   #untuk sort berdasar tanggal
        'country': 'id',
        'sVi': '',
        'candidateId': 19089307,
        'solVisitorId': 'a11ab7d5-1fe8-4fb3-acfb-41ff8c716f0d',
        'categories': [],
        'workTypes': [],
        'userAgent': 'Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/109.0.0.0%20Safari/537.36',
        'industries': [],
        'locale': 'id',
    },
}

req = requests.post('https://xapi.supercharge-srp.co/job-search/graphql', params=params, headers=headers, json=json_data).json()

def get_json():
    totjob = int(req['data']['jobs']['solMetadata']['totalJobCount'])
    szpg = int(req['data']['jobs']['solMetadata']['pageSize'])
    totpg = int(totjob//szpg)
    print("Total Page : ", totpg)
    # print(totjob)
    # print(szpg)
    # totpg = int(input("Input Jumlah Page yang akan di Scrap : "))
    
    pgjson = []
    for i in range(1, totpg+1):
        pg = {
            'query': 'query getJobs($country: String, $locale: String, $keyword: String, $createdAt: String, $jobFunctions: [Int], $categories: [String], $locations: [Int], $careerLevels: [Int], $minSalary: Int, $maxSalary: Int, $salaryType: Int, $candidateSalary: Int, $candidateSalaryCurrency: String, $datePosted: Int, $jobTypes: [Int], $workTypes: [String], $industries: [Int], $page: Int, $pageSize: Int, $companyId: String, $advertiserId: String, $userAgent: String, $accNums: Int, $subAccount: Int, $minEdu: Int, $maxEdu: Int, $edus: [Int], $minExp: Int, $maxExp: Int, $seo: String, $searchFields: String, $candidateId: ID, $isDesktop: Boolean, $isCompanySearch: Boolean, $sort: String, $sVi: String, $duplicates: String, $flight: String, $solVisitorId: String) {\n  jobs(\n    country: $country\n    locale: $locale\n    keyword: $keyword\n    createdAt: $createdAt\n    jobFunctions: $jobFunctions\n    categories: $categories\n    locations: $locations\n    careerLevels: $careerLevels\n    minSalary: $minSalary\n    maxSalary: $maxSalary\n    salaryType: $salaryType\n    candidateSalary: $candidateSalary\n    candidateSalaryCurrency: $candidateSalaryCurrency\n    datePosted: $datePosted\n    jobTypes: $jobTypes\n    workTypes: $workTypes\n    industries: $industries\n    page: $page\n    pageSize: $pageSize\n    companyId: $companyId\n    advertiserId: $advertiserId\n    userAgent: $userAgent\n    accNums: $accNums\n    subAccount: $subAccount\n    minEdu: $minEdu\n    edus: $edus\n    maxEdu: $maxEdu\n    minExp: $minExp\n    maxExp: $maxExp\n    seo: $seo\n    searchFields: $searchFields\n    candidateId: $candidateId\n    isDesktop: $isDesktop\n    isCompanySearch: $isCompanySearch\n    sort: $sort\n    sVi: $sVi\n    duplicates: $duplicates\n    flight: $flight\n    solVisitorId: $solVisitorId\n  ) {\n    total\n    totalJobs\n    relatedSearchKeywords {\n      keywords\n      type\n      totalJobs\n    }\n    solMetadata\n    suggestedEmployer {\n      name\n      totalJobs\n    }\n    queryParameters {\n      key\n      searchFields\n      pageSize\n    }\n    experiments {\n      flight\n    }\n    jobs {\n      id\n      adType\n      sourceCountryCode\n      isStandout\n      companyMeta {\n        id\n        advertiserId\n        isPrivate\n        name\n        logoUrl\n        slug\n      }\n      jobTitle\n      jobUrl\n      jobTitleSlug\n      description\n      employmentTypes {\n        code\n        name\n      }\n      sellingPoints\n      locations {\n        code\n        name\n        slug\n        children {\n          code\n          name\n          slug\n        }\n      }\n      categories {\n        code\n        name\n        children {\n          code\n          name\n        }\n      }\n      postingDuration\n      postedAt\n      salaryRange {\n        currency\n        max\n        min\n        period\n        term\n      }\n      salaryVisible\n      bannerUrl\n      isClassified\n      solMetadata\n    }\n  }\n}\n',
            'variables': {
            'keyword': cari,
            'jobFunctions': [],
            'locations': [
                32900,
                30501,
            ],
            'salaryType': 1,
            'jobTypes': [],
            'createdAt': None,
            'careerLevels': [],
            'page': i,
            'sort': 'createdAt',    #untuk sort berdasar tanggal
            'country': 'id',
            'sVi': '',
            'candidateId': 19089307,
            'solVisitorId': 'a11ab7d5-1fe8-4fb3-acfb-41ff8c716f0d',
            'categories': [],
            'workTypes': [],
            'userAgent': 'Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/109.0.0.0%20Safari/537.36',
            'industries': [],
            'locale': 'id',
            },
}
        pgjson.append(pg)
    return pgjson


def all_jobs(pg, cari):
    json_data = pg
    reqa = requests.post('https://xapi.supercharge-srp.co/job-search/graphql', params=params, headers=headers, json=json_data).json()
    rows = reqa['data']['jobs']['jobs']
    
    id_all = []
    for i in range(0, len(rows)):
        tit = rows[i]['jobTitleSlug']
        pss = re.findall(cari, tit)
        if pss:
            id = rows[i]['id']
            id_all.append(id)
            
    return id_all
    

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def job_detail(id):  
    headers = {
        'authority': 'xapi.supercharge-srp.co',
        'accept': '*/*',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://www.jobstreet.co.id',
        'referer': 'https://www.jobstreet.co.id/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    params = {
        'country': 'id',
        'isSmartSearch': 'true',
    }

    json_data = {
        'query': 'query getJobDetail($jobId: String, $locale: String, $country: String, $candidateId: ID, $solVisitorId: String, $flight: String) {\n  jobDetail(\n    jobId: $jobId\n    locale: $locale\n    country: $country\n    candidateId: $candidateId\n    solVisitorId: $solVisitorId\n    flight: $flight\n  ) {\n    id\n    pageUrl\n    jobTitleSlug\n    applyUrl {\n      url\n      isExternal\n    }\n    isExpired\n    isConfidential\n    isClassified\n    accountNum\n    advertisementId\n    subAccount\n    showMoreJobs\n    adType\n    header {\n      banner {\n        bannerUrls {\n          large\n        }\n      }\n      salary {\n        max\n        min\n        type\n        extraInfo\n        currency\n        isVisible\n      }\n      logoUrls {\n        small\n        medium\n        large\n        normal\n      }\n      jobTitle\n      company {\n        name\n        url\n        slug\n        advertiserId\n      }\n      review {\n        rating\n        numberOfReviewer\n      }\n      expiration\n      postedDate\n      postedAt\n      isInternship\n    }\n    companyDetail {\n      companyWebsite\n      companySnapshot {\n        avgProcessTime\n        registrationNo\n        employmentAgencyPersonnelNumber\n        employmentAgencyNumber\n        telephoneNumber\n        workingHours\n        website\n        facebook\n        size\n        dressCode\n        nearbyLocations\n      }\n      companyOverview {\n        html\n      }\n      videoUrl\n      companyPhotos {\n        caption\n        url\n      }\n    }\n    jobDetail {\n      summary\n      jobDescription {\n        html\n      }\n      jobRequirement {\n        careerLevel\n        yearsOfExperience\n        qualification\n        fieldOfStudy\n        industryValue {\n          value\n          label\n        }\n        skills\n        employmentType\n        languages\n        postedDate\n        closingDate\n        jobFunctionValue {\n          code\n          name\n          children {\n            code\n            name\n          }\n        }\n        benefits\n      }\n      whyJoinUs\n    }\n    location {\n      location\n      locationId\n      omnitureLocationId\n    }\n    sourceCountry\n  }\n}\n',
        'variables': {
            'jobId': str(id),
            'country': 'id',
            'locale': 'id',
            'candidateId': '19089307',
            'solVisitorId': 'a11ab7d5-1fe8-4fb3-acfb-41ff8c716f0d',
        },
    }

    resp = requests.post('https://xapi.supercharge-srp.co/job-search/graphql', params=params, headers=headers, json=json_data).json()
    
    if resp['data']['jobDetail'] is not None:
        row = resp['data']['jobDetail']
    else:
        print('none')

    
    nm = row['header']['company']
    if 'name' not in nm or nm['name'] == None or nm['name'] == "":
        nama = "Dirahasiakan"
    else:
        nama = row['header']['company']['name']
        
    jobtitle = row['header']['jobTitle']
    
    status = row['jobDetail']['jobRequirement']['employmentType']
    if status == None or status == "":
        status = "-"
        
    pendidikan = row['jobDetail']['jobRequirement']['qualification']
    
    alamat = row['companyDetail']['companySnapshot']['nearbyLocations']
    if alamat == None or alamat == "":
        alamat = "-"
        
    loks = []
    for e in range(0, len(row['location'])):
        lok = row['location'][e]['location']
        if lok == None:
            lok = ""
        loks.append(lok)
    loks = ' | '.join([str(elem) for elem in loks])
    
    gaji = row['header']['salary']['min']
    if gaji == None:
        gaji = ""
    gj = row['header']['salary']['max']
    if gj == None:
        gj = ""
    gaji = str(gaji)+" - "+str(gj)
    
    level = row['jobDetail']['jobRequirement']['careerLevel']
    if level == None or level == "":
        level = "-"
        
    pengalaman = row['jobDetail']['jobRequirement']['yearsOfExperience']
    if pengalaman == None or pengalaman == "":
        pengalaman = "-"
    
    size = row['companyDetail']['companySnapshot']['size']  
    if size == None or size == "":
        size = "-"
        
    deskripsi = row['jobDetail']['jobDescription']
    postdate = row['jobDetail']['jobRequirement']['postedDate']
    closedate = row['jobDetail']['jobRequirement']['closingDate']  
    
    if row['jobDetail']['jobRequirement']['industryValue'] is not None:
        industri = row['jobDetail']['jobRequirement']['industryValue']['label']
    else:
        industri = "-"
    
    link = row['pageUrl']
      
    print('Posisi       :', jobtitle)
    print('Perusahaan   :', nama)
    print('Penempatan   :', loks)
    print('Alamat kantor:', alamat)
    print('Tgl Post     :', postdate[0:12])
    print('Tgl Close    :', closedate[0:10])
    print('Gaji         :', gaji)
    print('Link         :', link)
    
    print('---------------------------------------------')
    return 

if __name__ == '__main__':
    jsn = get_json()
    all_data = []
    for i in range(0, len(jsn)):
        pg = jsn[i]
        # print(pg)
        data = all_jobs(pg,cari)
        # print(data)
        # print(i)
        all_data.extend(data)
    # print(all_data)
    c = len(all_data)
    print('Key Match :', c)
    # all_id = []
    jobrow = 0
    for j in range(0, len(all_data)):
        id = all_data[j]
        print(j+1)
        job_detail(id)
        #print(id)
        # all_id.extend(dtl)      
        
        jobrow += 1
        if jobrow >= 5:
            ln = input(f'Tampilkan 5 job lagi... (y/n)')
            if ln == 'n':
                break
            else:
                print('==================================================================')
                jobrow = 0

    
    
 


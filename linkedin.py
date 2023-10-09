import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.linkedin.com/jobs/search/?currentJobId=3735895362&geoId=104370960&keywords=Administration&location=Jakarta%20Raya%2C%20Indonesia')
print(response)

soup = BeautifulSoup(response.text, "lxml")
print(soup.title)

a_href=soup.findAll("a",{"class":"disabled ember-view job-card-container__link job-card-list__title"})
lis = []
for lk in a_href:
    # link = burl+a_href['href'].text
   print(lk)

# class="flex-grow-1 artdeco-entity-lockup__content ember-view">
# <a data-control-id="5S7XZVAawSVXD9HYIKaDcA==" tabindex="0" href="/jobs/view/3735895362/?eBP=CwEAAAGLEy8U8F5GVhI-Jp59xvFixIG3lwG6CiHFg8MKkwUBnyONMKDikxuPKNysHTcOAYNHe3rUlPAAtvbO5P0PnlZ1vZMZwCpC3p67pCzYrfvWqR8WtU-z8XCxIuHM7fhEbWLFTgB8W2pfXIf_diLpKnP0Qqya7GZuD_63v-UEWcRVOeHLCd7f9Ac9lpZ5LX94_T5KitjQ-3usdEEG2SOCQaAsMQ_XIuAYYkdYkEyKHf2Hf9hfFFjtjJh-9CnLofuJpG_UmYoRisqcoyMJ9_68JeOg2FfS7JVePxNf-z3ay6yozeVyZodPpIjOj2d5f4njkXmx2YwwSkRA3ZdF-dSsUFY6lGRyO6NB9kHZalqgNlL4hzvBYIsyT9kxczRcctI8JUg9LO2LHSjNNk9liMDKsdfd1ZnFoKwz&amp;refId=bivVqrzhERYL0bT8URkYjg%3D%3D&amp;trackingId=5S7XZVAawSVXD9HYIKaDcA%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember668" class="<a data-control-id="5S7XZVAawSVXD9HYIKaDcA==" tabindex="0" href="/jobs/view/3735895362/?eBP=CwEAAAGLEy8U8F5GVhI-Jp59xvFixIG3lwG6CiHFg8MKkwUBnyONMKDikxuPKNysHTcOAYNHe3rUlPAAtvbO5P0PnlZ1vZMZwCpC3p67pCzYrfvWqR8WtU-z8XCxIuHM7fhEbWLFTgB8W2pfXIf_diLpKnP0Qqya7GZuD_63v-UEWcRVOeHLCd7f9Ac9lpZ5LX94_T5KitjQ-3usdEEG2SOCQaAsMQ_XIuAYYkdYkEyKHf2Hf9hfFFjtjJh-9CnLofuJpG_UmYoRisqcoyMJ9_68JeOg2FfS7JVePxNf-z3ay6yozeVyZodPpIjOj2d5f4njkXmx2YwwSkRA3ZdF-dSsUFY6lGRyO6NB9kHZalqgNlL4hzvBYIsyT9kxczRcctI8JUg9LO2LHSjNNk9liMDKsdfd1ZnFoKwz&amp;refId=bivVqrzhERYL0bT8URkYjg%3D%3D&amp;trackingId=5S7XZVAawSVXD9HYIKaDcA%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember668" class="disabled ember-view job-card-container__link job-card-list__title" aria-label="Product Sales Specialist (Hotel PMS software)">
                  # Product Sales Specialist (Hotel PMS software)
                # </a>" aria-label="Product Sales Specialist (Hotel PMS software)">
                  # Product Sales Specialist (Hotel PMS software)
                # </a>
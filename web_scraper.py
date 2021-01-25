
import json
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError



URL = 'https://www.monster.com/jobs/search/?q=Entry-Level-Software-Developer&where=Atlanta__2C-GA&intcid=skr_navigation_nhpso_searchMain'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
for url in response:
    try:
        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error has occurred: {http_err}')
    
    except Exception as err:
        print(f'Other error has occurred: {err}')

    else:
        print('Success!!')
        break

job_arr = []

for job in soup.find('div', attrs= {'id': 'SearchResults'}).select('section.card-content:not(.apas-ad)'):
    job_object = {
        'Job Titles': job.find('h2', attrs={'class': 'title'}).text.strip(),
        'Locations': job.select('.location .name')[0].text.strip(),
        'Companies': job.find('div', attrs={'class': 'company'}).text.strip(),
        'Links': job.find('a')['href']
    }
    job_arr.append(job_object) 

with open('job_data.json', 'w') as outfile:
    json.dump(job_arr, outfile)

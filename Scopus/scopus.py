import requests
import logging
import csv
from random import randint
import time

SCRAPEOPS_API_KEY = "api_key"

def get_user_agent_list():
  response = requests.get('http://headers.scrapeops.io/v1/user-agents?api_key=' + SCRAPEOPS_API_KEY)
  json_response = response.json()
  return json_response.get('result', [])

def get_random_user_agent(user_agent_list):
  random_index = randint(0, len(user_agent_list) - 1)
  return user_agent_list[random_index]

query = "employee mental health in organizations"
items_per_page = 25
url = "http://api.elsevier.com/content/search/scopus"


logging.basicConfig(filename='extraction_log.txt', level=logging.INFO)

def total_results():
    params = {
        'query': query
    }
    headers = {
                "X-ELS-APIKey": "8d55ace239d6fe4ea6c451049b2ce270",
                "Content-Type": "application/json"
    }
    response = requests.get(url,headers=headers,params=params)
    data = response.json()
    return data['search-results']['opensearch:totalResults']
     
def get_results(start_index,headers):
    params = {
        'query': query,
        'start': start_index,
        'count': items_per_page
    }
    response = requests.get(url,headers=headers,params=params)
    return response.json()

def save_title_to_csv(title):
    with open('scopus_results.csv', 'a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([title]) 
        

def extract_pages():
    user_agent_list = get_user_agent_list()

    results = int(total_results())
    print(results)
    page_num = 1
    for i in range(0,results,items_per_page):
        time.sleep(2)
        headers = {
                "X-ELS-APIKey": "8d55ace239d6fe4ea6c451049b2ce270",
                "Content-Type": "application/json",
                "User-Agent": get_random_user_agent(user_agent_list)
              }
        data = get_results(i,headers)

        for entry in data['search-results']['entry']:
            title = entry.get('dc:title', 'No Title')
            save_title_to_csv(title)

        logging.info(f"Page {page_num} processed successfully.")
        print(f"Page {page_num} processed successfully")
        page_num += 1

if __name__ == "__main__":
    extract_pages()
    print("All results have been saved.")

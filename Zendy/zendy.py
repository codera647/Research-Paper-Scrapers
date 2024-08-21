import requests
import csv
import time
import logging
import re
from random import randint

Scrap_ops_Api = "559edec8-44f0-47f1-9736-3f8b9a66bab7"

def get_headers_list():
  response = requests.get('http://headers.scrapeops.io/v1/browser-headers?api_key=' + Scrap_ops_Api)
  json_response = response.json()
  return json_response.get('result', [])

def get_random_header(header_list):
  random_index = randint(0, len(header_list) - 1)
  return header_list[random_index]


logging.basicConfig(filename='extraction_log2.txt', level=logging.INFO)

url = "https://api.zendy.io/search/search"
headers = {
    "Content-Type": "application/json"
}

search_query = {
    "searchQuery": [{"term": "employee mental health"}],
    "sortFilters": "relevance",
    "filters": [],
    "dateFilters": {"start": "1000-1", "end": "2050-12", "appliedFromDate": False, "appliedToDate": False},
    "facetFilters": [{"categoryId": "subjectsFull", "facetLabel": "Business and Economics", "active": True, "categoryLabel": "subjectsFull"}],
    "pageNumber": 1
}

total_pages = 70275
def clean_html_tags(text):
   
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text  

def save_title_to_csv(index,title):
    clean_title = clean_html_tags(title)
    with open('zendy_titles.csv', 'a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([index,clean_title.encode('utf-8', 'ignore').decode('utf-8')])

def extract_titles_from_page(page_number,header_list):
    search_query['pageNumber'] = page_number
    try:
        response = requests.post(url, json=search_query, headers=get_random_header(header_list))
        response.raise_for_status()
        data = response.json()

        titles = [result["title"] for result in data["data"]["searchResults"]["results"]]
        for i, title in enumerate(titles, start=(page_number - 1) * 10 + 1):  
            save_title_to_csv(i, title)

        logging.info(f"Page {page_number} processed successfully.")
        print(f"Page {page_number} processed successfully.")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error on page {page_number}: {e}")
        print(f"Error on page {page_number}: {e}")
        time.sleep(10)  
        extract_titles_from_page(page_number)

def main():
    header_list = get_headers_list()
    for page in range(1, total_pages + 1):
        extract_titles_from_page(page,header_list)
        time.sleep(1) 

if __name__ == "__main__":
    main()

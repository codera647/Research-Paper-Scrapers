from scholarly import scholarly
from scholarly import ProxyGenerator
import time
import csv
import logging




logging.basicConfig(filename='extraction_log.txt', level=logging.INFO)

def save_to_csv(title):

        with open('google_scholar_titles.csv', 'a', newline='',encoding='utf-8') as file:
           writer = csv.writer(file)
           writer.writerow([title.encode('utf-8', 'ignore').decode('utf-8')])

def search_for_publications():

    pg = ProxyGenerator()
    success = pg.FreeProxies()
    print(success)
    scholarly.use_proxy(pg)
    search_query = scholarly.search_pubs(query ='HR management' , year_low='2020',year_high='2024')
    index = 1
    page_number = 1
    for pub in search_query:
        title = pub['bib']['title']
        # time.sleep(5)
        save_to_csv(title)
        index += 1
        if(index == 10):
           logging.info(f"Page Number {page_number} processed successfully.")
           print(f"Page {page_number} procced successfully")
           page_number += 1
           index = 1


if __name__ == "__main__":
    search_for_publications()
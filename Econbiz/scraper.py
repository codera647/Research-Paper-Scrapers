from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from random import choice
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/90.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
]

def initialize_driver(user_agent):
    options = Options()
    # options.add_argument("--headless")  
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    options.add_argument(f"user-agent={user_agent}")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_econbiz(num_pages):
    user_agent = choice(user_agents)
    driver = initialize_driver(user_agent)
    driver.get('https://www.econbiz.de/Search/Results?lookfor=employee+mental+health&type=AllFields&limit=10&sort=relevance')
  

    titles = []
    for _ in range(num_pages):
        results = driver.find_elements(By.CSS_SELECTOR, 'a.title.print-no-url') 
        for result in results:
            title = result.get_attribute('title')
            if title:
                titles.append(title)
        if num_pages>=1:
                try:
                    next_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.pagination-next a'))
                    )
                    next_button.click()
                    time.sleep(5)  
                except Exception as e:
                    print(f"Error navigating to the next page: {e}")
                    break

    driver.quit()
    return titles

def main():
    num_pages = int(input("Enter the number of pages to extract: "))

    file_exists = os.path.isfile("econbiz_titles.csv")
    titles = scrape_econbiz(num_pages)
    
    if file_exists:
        df_existing = pd.read_csv("econbiz_titles.csv")
        existing_titles = df_existing['Title'].tolist()
        new_titles = [title for title in titles if title not in existing_titles]
        df_new = pd.DataFrame(new_titles, columns=["Title"])
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = pd.DataFrame(titles, columns=["Title"])

    df_combined.to_csv("econbiz_titles.csv", index=False)
    print(f"Extracted {len(titles)} titles and saved to econbiz_titles.csv")

if __name__ == "__main__":
    main()

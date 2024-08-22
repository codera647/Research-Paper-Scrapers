# Scopus Web Scraper

This Python script is designed to scrape research article titles related to "employee mental health in organizations" from the Scopus database using the Elsevier API. The script extracts the titles of research articles and saves them to a CSV file.

## Features

- **API Integration**: Uses the Elsevier Scopus API to search and retrieve research articles.
- **User-Agent Rotation**: Utilizes ScrapeOps to fetch a list of user agents and randomly select one for each API request to avoid being blocked.
- **CSV Output**: Saves the extracted article titles in a CSV file named `scopus_results.csv`.
- **Logging**: Logs the progress of the extraction process in a log file named `extraction_log.txt`.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Required Python packages

You can install the required packages using pip:

```bash
pip install requests
```
## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/scopus-web-scraper.git
   cd scopus-web-scraper
   ```
2. **Set Up API Keys**

1. Replace `SCRAPEOPS_API_KEY` with your ScrapeOps API key in the `get_user_agent_list` function.

2. Replace `"X-ELS-APIKey"` in the `headers` dictionary with your Elsevier Scopus API key.


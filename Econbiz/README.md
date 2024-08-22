# EconBiz Web Scraper

This Python project is a web scraper designed to extract article titles from the [EconBiz](https://www.econbiz.de/) website. The script automates the process of collecting data related to employee mental health research by navigating through multiple pages of search results and saving the extracted titles to a CSV file.

## Features

- **Multiple Page Navigation:** Automatically navigates through multiple pages of search results on EconBiz.
- **User-Agent Rotation:** Uses random user-agent strings to reduce the likelihood of being blocked by the website.
- **CSV File Handling:** Saves extracted titles to a CSV file. If the file already exists, new titles are appended without duplication.
- **Error Handling:** Includes basic error handling for issues like navigation failures.

## Prerequisites

Before running the script, you'll need to have the following installed:

- **Python 3.x**
- **Google Chrome browser**
- **ChromeDriver**

### Required Python Packages

Install the required Python packages using `pip`:

```bash
pip install selenium webdriver-manager pandas
```
## Usage

### Clone the Repository

```bash
git clone https://github.com/codera647/Research-Paper-Scraper/Econbiz/scraper.git
cd scraper
```

### Run the Script

Start the scraping process by running the script:

```bash
python scraper.py

```

### Output
The extracted titles will be saved in a file named `econbiz_titles.csv`. If the file already exists, the script will append new titles to it, avoiding duplicates.

### File Structure
- `scraper.py`: The main script that handles the web scraping process.
- `econbiz_titles.csv`: The output file where the extracted titles are saved (generated after the first run).

### Code Overview
- **User-Agent Randomization**: The script randomly selects a user-agent string from a predefined list to mimic different browser profiles.
- **Navigation**: The script navigates through the search results pages by clicking the "Next" button, until it reaches the specified number of pages.
- **Data Extraction**: The script extracts the title of each article on the current page.
- **Data Storage**: The titles are stored in a CSV file. If the file already exists, the script checks for duplicates and appends only new titles.

### Dependencies
- **Selenium**: Used for automating the web browser.
- **webdriver-manager**: Automatically manages the ChromeDriver binaries.
- **pandas**: Used for handling and manipulating CSV files.

### Error Handling
The script includes basic error handling for issues like:

- **Navigation Failures**: If the script fails to navigate to the next page, it will print an error message and stop.
- **File Handling**: The script checks if the CSV file exists before appending new data, ensuring no data is lost.

### Contributing
Feel free to submit issues or pull requests if you have suggestions for improvements or find any bugs.

### Contact
For any questions or inquiries, please contact `codera647@gmai.com`.


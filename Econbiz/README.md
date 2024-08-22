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

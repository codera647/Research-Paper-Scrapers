
# Introduction

This repository contains Python scripts designed to scrape research paper titles from various websites. Whether you're looking to extract titles for academic research, data analysis, or simply to stay updated with the latest publications, these scrapers provide an efficient and automated solution. Each script is tailored to handle different website structures, ensuring accurate and reliable extraction of information. Contributions and improvements are welcome to enhance the repository's functionality and coverage.




## Websites

1. **<u>Econbiz:</u>** <br>
 [EconBiz](https://www.econbiz.de) is a service of the ZBW - Leibniz Information Centre for Economics. That support you with your search for scholarly information. Thet don't specifically provide any *Api Endpoints* to extract data so I use [Selenium](https://www.selenium.dev/documentation/) to scrap research papers and articles.

2. **<u>Google Scholar:</u>** <br>
  [Google Scholar](https://scholar.google.com/schhp?hl=en) provides a simple way to broadly search for scholarly literature. Although there is no official *Google Scholar Api* but there are third-party solutions like [Scholarly](https://github.com/scholarly-python-package/scholarly) Python package which supports profile, author, cite and organic results (search_pubs seems to be the method to get organic results, although method name confuses me).

3. **<u>Scopus:</u>** <br>
  [Scopus](https://www.elsevier.com/products/scopus) is a database that offers a comprehensive overview of global interdisciplinary scientific information, covering the areas of science, technology, medicine, social sciences and the arts and humanity. There is a solution named [Scopus Search Api](https://dev.elsevier.com/documentation/ScopusSearchAPI.wadl) provided by [Elsevier Developer Portal](https://dev.elsevier.com) that assist you to get access to scopus open-source database.

4. **<u>Zendy:</u>** <br>
  [Zendy](https://zendy.io) offers a blended discovery experience where you can read and download open access and paywalled research from the world’s leading publishers on one platform. Using zendy api we can access variety of articles and research papers.


## Acknowledgements

- **Contributors**: Special thanks to all contributors specially **@ziadcoolio** who helped in the development and improvement of this project.
- **Open-Source Projects**: This project was made possible by various open-source tools and libraries, including [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), [Requests](https://requests.readthedocs.io/), and [Selenium](https://www.selenium.dev/).
- **Documentation Resources**: Thanks to the authors of various documentation and tutorials that guided the development process.


# Scraping with Selenium
Web scraping using Python and Selenium.

## Overview
This project is to be my reference for scraping with Python and Selenium. Should you find anything useful here, please feel free to use it as you see fit.

## Getting Started
This project was written using Python 3 (3.8.2 specifically). Ensure that Python is installed and properly configured.

__Clone the repository and install dependencies__

`user@machine:~/Workspace$ git clone https://github.com/KyleEgland/python_scraping_selenium.git`

`user@machine:~/Workspace$ cd python_scraping_selenium/`

_Note: This project was developed using the `virtualenv` Python module. Should you use a different virtual environment setup, please substitute the appropriate command_

`user@machine:~/Workspace/python_scraping_selenium$ python -m virtualenv env`

`user@machine:~/Workspace/python_scraping_selenium$ source ./env/bin/activate`

_Note: to activate on Windows use the command `. .\env\Scripts\activate` in PS or `\env\Scripts\activate` in the cmd prompt_

`(env) user@machine:~/Workspace/python_scraping_selenium$ python -m pip install -r requirements.txt`

__Get Browser Driver(s)__

Use the links in the Drivers section to obtain

__Running the Examples__

`(env) user@machine:~/Workspace/python_scraping_selenium$ python `

## Drivers
Use the links below to get the appropriate browser driver:

* [Firefox (geckodriver)](https://github.com/mozilla/geckodriver)
* [Chrome (ChromeDriver)](https://chromedriver.chromium.org/downloads)

## Notes on scraping

Please be responsible when scraping the internet.  While the resources that are open to the public are just that, they also come at a cost and are not all maintained by faceless organizations. This repository is not an endorsement of indescriminantly crawling the web but rather a resources for how to conduct scraping.

## Credits

* [Web Scraping using Selenium and Python](https://www.scrapingbee.com/blog/selenium-python/)
* [Beginner's Guide to Web Scraping with Python's Selenium](https://lewiskori.com/blog/beginner-s-guide-to-web-scraping-with-python-s-selenium/)

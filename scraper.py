#! python
#
# Scraper
import argparse
import os
import re
import sys


# --------------
# Selenium Setup
# --------------
# Check for the existence of the drivers path by getting the current working
# directory and appending "drivers"
driver_directory = os.path.join(os.getcwd(), "drivers")
if not os.path.exists(driver_directory):
    print(f"\n[ ! ] Please put drivers in {driver_directory} directory\n")
    sys.exit(1)

# Initializing webdriver variable - Only one is needed, the code below is
# simply to allow for either.
webdriver = ""

# Checking for the Firefox driver. Note that the file name may differ based on
# release. This code may also be replaced, simply hard-coding in the
# appropriate driver.
if os.path.isfile(os.path.join(driver_directory, "geckodriver.exe")):
    from selenium.webdriver import Firefox
    webdriver = os.path.join(driver_directory, "geckodriver.exe")
    driver = Firefox(executable_path=webdriver)
    print("\n[ + ] Using Firefox webdriver\n")

# Checking for the Chrome driver. Note that the file name may differ based on
# release. This code may also be replaced, simply hard-coding in the
# appropriate driver.
elif os.path.exists(os.path.join(driver_directory, "chromedriver.exe")):
    from selenium.webdriver import Chrome
    webdriver = os.path.join(driver_directory, "chromedriver.exe")
    driver = Chrome(webdriver)
    print("\n[ + ] Using Chrome webdriver\n")
# ==================
# End Selenium Setup
# ==================


# -----------
# Arg parsing
# -----------
# scraper.py is intended to be a command-line utility so it uses the argparse
# package to take in varibles (required and optional arguments) supplied by the
# user to execute the rest of the program.

# Setting a global variable for URL checking
# Regex from the django repository:
# https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45
url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  #domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE
)


def url(input_url):
    # url type validation function - argparse will pass in values received via
    # the "target" argument in order for them to be validated by this function
    # Using the regex created previously to check the given input
    global url_regex

    if not url_regex.search(input_url):
        # Cannot proceed without a proper url
        msg = str(
            "[ ! ] Invalid URL given; use valid format:\n"
            "https://example.com\n"
            "http://www.example.com\n"
            "http://localhost:8080/site.html"
        )
        raise argparse.ArgumentTypeError(msg)
    return input_url


# Instantiate argument parser
parser = argparse.ArgumentParser(
    description="Selenium scraper example"
)

# Adding arguments
#
# Target - the site that is to be accessed via the scraper
parser.add_argument(
    "target",
    type=url,
    help="Scraper target site (e.g. https://example.com)"
)

# Parse the given arguments
args = parser.parse_args()

print(args)

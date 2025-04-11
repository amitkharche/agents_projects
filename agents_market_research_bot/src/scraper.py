"""
Web scraper module using Selenium and BeautifulSoup.
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def init_driver():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)

def fetch_content(url, wait=3):
    driver = init_driver()
    driver.get(url)
    time.sleep(wait)
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

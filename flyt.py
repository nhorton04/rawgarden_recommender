import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

from itertools import islice
import wget
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

import requests
from bs4 import BeautifulSoup
import time, os



chromedriver = "/usr/bin/chromedriver" # path to the chromedriver executable
os.environ["webdriver.chrome.driver"] = chromedriver
url = 'https://www.flytdelivery.com/menu?dtche%5Bsearch%5D=raw+garden&dtche%5Bcategory%5D=concentrates'

i = 1

driver = webdriver.Chrome(chromedriver)
driver.get(url)

elem = driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div/div[1]/div/div/span[1]')


elem.click()

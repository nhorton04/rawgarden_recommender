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

chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
url = "https://rawgarden.farm/labresults"

def raw(scrains):
    i = 0
    while i < len(scrains):
        results = {
        'THCa': [],
        'D9THC': [],
        'CBD': [],
        'Terpinolene': [],
        'α-Pinene': [],
        'β-Pinene': [],
        'Linalool': [],
        'Limonene': [],
        'β-Myrcene': [],
        'β-Caryophyllene': [],
        'Ocimene': [],
        'α-Humulene': [],
        'Isopulegol': [],
        'trans-Nerolidol': [],
        'δ-Limonene': [],
        'λ-Limonene': [],
        'Guaiol': [],
        'Eucalyptol': [],
        'Camphene': [],
        'Geraniol': [],
        'α-Terpinene': [],
        'γ-Terpinene': [],
        'p-Cymene': [],
        'α-Bisabolol': [],
        'δ-3-Carene': [],
        'Camphor': [],
        'Fenchone': [],
        'Pulegone': [],
        'Sabinene hydrate': [],
        'Borneol': [],
        'Trans beta farnesene': [],
        'Valencene': [],
        'Sabinene': [],
        'Gamma terpinene': [],
        'THCv': [],
        'D8THC': [],
        'CBDa': [],
        'CBDv': [],
        'CBGa': [],
        'CBG': [],
        'CBN': [],
        'CBC': [],
        'Fenchol': [],
        'Limonene': [],
        'Ocimene 1': [],
        'Ocimene 2': [],
        'Menthol': [],
        'Isoborneol': [],
        'Cedrol': [],
        'Geranyl acetate': [],
        'P-mentha-1,5-diene': [],
        'Gamma terpinene': [],
        '3-Carene': [],
        'α-Cedrene': []}

        for scrain in scrains[i:]:
            driver = webdriver.Chrome(chromedriver)
            driver.get(url)
            WebDriverWait(driver, 10)
            close_popup(driver)
            perform_search(scrain, driver)
            click_first_element(driver)
            read_pdf(driver)
            driver.quit()
            i += 1

def perform_search(scrain, driver):
    search_box = driver.find_element_by_xpath('//*[@id="myInput"]')
    WebDriverWait(driver, 10)
    search_box.clear()
    search_box.send_keys(scrain)
    search_box.send_keys(Keys.RETURN)

def close_popup(driver):
    yes_button = driver.find_element_by_xpath('//*[@id="modal_content_wrapper"]/nav/ul/li[1]/a')
    yes_button.click()

def click_first_element(driver):
    first_element = driver.find_element_by_xpath('//*[@id="myUL"]/li[8]/a')
    first_element.click()


def read_pdf(driver):
    page = driver.current_url
    resp = requests.get(page)


raw(['Kush', 'Haze'])
# fd = open("gps.pdf", "rb")
# doc = PDFDocument(fd)
# viewer = SimplePDFViewer(fd)
#
# page_one = next(doc.pages())
# all_pages = [p for p in doc.pages()]
#
# viewer.navigate(1)
# viewer.render()
# print(viewer.canvas.strings)

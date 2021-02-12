import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrall():
    url="https://scomb.shibaura-it.ac.jp/portal/dologin?initialURI="
    driver=webdriver.Chrome('./chromedriver.exe')
    driver.get(url)
    time.sleep(20)

    driver.find_element_by_id('continueButton').click()
    time.sleep(2)

    driver.find_element_by_id('navi-lms').click()
    time.sleep(2)

    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("div",attrs={'class':'calenderLayout'})
    df_table = pd.read_html(str(table))[0]

    df_table.to_pickle('class.pkl')

    driver.close()
    return 

import time
import chromedriver_binary
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrall():
    url="" # 大学のログインサイトのurlを入力してください
    driver=webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(100)
    driver.get(url)

    driver.find_element_by_id('continueButton').click()

    driver.find_element_by_id('navi-lms').click()

    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("div",attrs={'class':'calenderLayout'})
    
    df_table = pd.read_html(str(table))[0]

    df_table.to_pickle('class.pkl')

    driver.close()
    return 

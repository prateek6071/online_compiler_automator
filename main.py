# import web driver
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl.workbook import Workbook
# specifies the path to the chromedriver.exe
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
driver.get('https://www.onlinegdb.com')

def compiler(language,filename):
    text = driver.find_element_by_id('lang-select')
    print(text.text)
    select = Select(text)
    select.select_by_value(''+str(language))
    driver.implicitly_wait(2)
    new_file = driver.find_element_by_id('control-btn-newfile')
    new_file.click()
    driver.implicitly_wait(2)
    new_file_name = driver.find_element_by_id('new_file_name')
    new_file_name.clear()
    new_file_name.send_keys(''+str(filename))

compiler('c','test')
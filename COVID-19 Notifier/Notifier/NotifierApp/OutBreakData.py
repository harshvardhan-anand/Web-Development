from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import threading

class Update():
    '''
    This class will get the data from covid19india.org. 
    Disclaimer: This scraper project is made only for educational purpose. This 
                website provides API so you should use the API for building your applications.
    '''
    def __init__(self):
        self._CHROMEDRIVER = r'E:\PROJ.RC\__operational files__\github repo\Python Projects\Artificial Intelligence\GUI_Automation\Whatsapp Automation\chromedriver.exe'
        self._html, driver = self._loadjs()
        # CLosing driver takes time so just creating a new thread.
        t1 = threading.Thread(target = driver.close())
        t1.start()
        
    def _loadjs(self):
        try:
            driver = webdriver.Chrome(executable_path=self._CHROMEDRIVER)
            driver.get('https://www.covid19india.org/')
            # locating the total case div
            element = ec.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[2]/div[1]'))
            # since website is based on react so we need to wait till website loads
            WebDriverWait(driver, 1).until(element)
            html = driver.page_source
        except Exception as e:
            # Even if there is a error in finding the element we really dont care about that. As we only need the source code
            print(e)
        finally:
            return html, driver

    def data(self):
        obj = bs(self._html, features="lxml")
        active = obj.find('', {"class": 'level-item is-active'}).h1.text
        new = obj.find('', {"class": 'level-item is-confirmed'}).h4.text[1:]
        total = obj.find('', {"class": 'level-item is-confirmed'}).h1.text
        return (total, new, active)
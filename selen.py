import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pprint import pprint

import pandas as pd
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def webdrive_init() -> webdriver.Chrome: 

    option = Options()
    option.add_experimental_option('debuggerAddress', '127.0.0.1:9527')
    dr = webdriver.Chrome(options=option)
    
    return dr

dr = webdrive_init()


url = 'https://www.rebas.tw/tournament/CPBL-2025-JO/firstbase/full'
dr.get(url)




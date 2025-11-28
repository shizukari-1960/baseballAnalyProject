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


if __name__ == '__main__':
    dr = webdrive_init()
    url = 'https://www.rebas.tw/tournament/CPBL-2025-JO/firstbase/full'
    dr.get(url)

    sleep(15) # wait loading
    
    def select_table(table_name: str):
        name_xpath = {
            '中職2025年': {
                'button': '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[8]/a[1]/button',
                'team_strike_button' : '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[1]',
                'team_pitch_button' : '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]',

                'league_atk_sumup_table' : '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div[2]/div/table[1]',
                'team_atk_sumup_table' : '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div[2]/div/table[2]',

                'league_strike_sumup_table' : '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div[2]/div/table[1]',
                'team_strike_sumup_table' : '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div[2]/div/table[2]',

                
            }
        }




import os
from time import sleep

import pandas as pd
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from xpathData import teams_alias, tags, button_tables_storage



os.chdir(os.path.dirname(os.path.abspath(__file__)))


def webdrive_init() -> webdriver.Chrome: 

    option = Options()
    option.add_experimental_option('debuggerAddress', '127.0.0.1:9527')
    dr = webdriver.Chrome(options=option)
    
    return dr



def get_table(team_name: str, tag_name:str, table_name: str) -> pd.DataFrame:
    """
    Select a designated table in website, and return a pd datafrome.
    
    :param team_name: team name, in alias.
    :type team_name: str
    :param tag_name: page tag name (pitch and strike), in alias.
    :type tag_name: str
    :param table_name: table name, in docs.
    :type table_name: str
    :return: table dataframe.
    :rtype: pd.DataFrame
    """
    if team_name not in teams_alias:
        raise ValueError(f'{team_name}不是一個可選的隊伍。')
    if tag_name not in tags:
        raise ValueError(f'{tag_name} 不是一個可選的表格種類。')
    if table_name not in button_tables_storage[team_name].keys():
        raise ValueError(f'{table_name}不是一個可選的表。')
    
    body = dr.find_element(By.XPATH, '//*[@id="app-content"]/div/div[1]')
    dr.execute_script("arguments[0].scrollIntoView(true);", body)

    dr.find_element(By.XPATH, button_tables_storage[team_name]['button']).click()#change team
    dr.find_element(By.XPATH, button_tables_storage[team_name][tag_name]).click() #change tag

    table = dr.find_element(By.XPATH, button_tables_storage[team_name][table_name]).get_attribute('outerHTML')

    dft = pd.read_html(table)[0]

    return dft


if __name__ == '__main__':
    dr = webdrive_init()
    #url = 'https://www.rebas.tw/tournament/CPBL-2025-JO/firstbase/full'
    #dr.get(url)

    #sleep(15) # wait loading
    
    print(get_table('CTBC', 'bat', 'bat_score_table'))

    


    




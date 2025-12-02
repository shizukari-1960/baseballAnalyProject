import os
from time import sleep
import gsheet
import selen

import pandas as pd
from pprint import pprint



os.chdir(os.path.dirname(os.path.abspath(__file__)))
def formatize():
    pass

def dataframe_to_list_matrix(df: pd.DataFrame) -> list[list]:
    """
    將 Pandas DataFrame 轉換為 Google Sheet 或 API 所需的 List Matrix (列表的列表) 格式。
    List Matrix 的第一行包含欄位名稱 (Header)。
    """
    # 1. 取得欄位名稱 (Header)
    headers = [df.columns.values.tolist()]
    # 2. 取得數據行 (Data Rows)
    data_rows = df.values.tolist()
    # 3. 將欄位名稱和數據合併
    list_matrix = headers + data_rows
    
    return list_matrix

#TODO: assign data range from url = 'https://www.rebas.tw/tournament/CPBL-2025-JO/firstbase/full'

def process_and_insert_table(
    dr: selen.webdriver.Chrome, 
    team_name: str, 
    tag_name: str, 
    table_name: str, 
    sheet_name: str, 
    start_cell: str, 
    delay: int = 1
):
    """
    執行單一表格的「擷取 -> 轉換 -> 寫入 Google Sheet」流程。

    :param dr: 已初始化的 WebDriver 實例。
    :param team_name: 要擷取的隊伍名稱 (例如 'B')。
    :param tag_name: 要擷取的數據標籤 (例如 'bat', 'pitch')。
    :param table_name: 要擷取的具體表格名稱。
    :param sheet_name: Google 試算表中的工作表名稱。
    :param start_cell: 開始寫入數據的單元格位置 (例如 'A1')。
    :param delay: 寫入 Google Sheet 後的延遲秒數 (預設 1 秒)。
    """
    print(f"--- 開始處理 {team_name} / {tag_name} / {table_name} ---")
    
    # 1. 擷取數據
    df = selen.get_table(
        dr=dr, 
        team_name=team_name, 
        tag_name=tag_name, 
        table_name=table_name,
        
    )
    print(f"   => 成功擷取 DataFrame (共 {len(df)} 行)。")
    
    # 2. 轉換格式
    data_list = dataframe_to_list_matrix(df)
    
    # 3. 寫入 Google Sheet
    gsheet.insert_matrix(
        sheet_name=sheet_name, 
        start_cell=start_cell, 
        data_list=data_list
    )
    print(f"   => 成功寫入 Google Sheet 到 {sheet_name}!{start_cell}。")
    
    # 4. 延遲
    if delay > 0:
        sleep(delay)
        print(f"   => 延遲 {delay} 秒完成。")
    
    return df

if __name__ == '__main__':
    dr = selen.webdrive_init()
    print(process_and_insert_table(
        dr=dr,
        team_name='B',
        tag_name='bat',
        table_name='bat_atk_table',
        sheet_name='batting',
        start_cell='A1',
        delay=2
    ))

    print(process_and_insert_table(
        dr=dr,
        team_name='B',
        tag_name='bat',
        table_name='bat_balls_table',
        sheet_name='batting',
        start_cell='T1',
        delay=2
    ))

    print(process_and_insert_table(
        dr=dr,
        team_name='B',
        tag_name='bat',
        table_name='bat_score_table',
        sheet_name='batting',
        start_cell='AN1',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='T',
        tag_name='bat',
        table_name='bat_atk_table',
        sheet_name='batting',
        start_cell='A30',
        delay=2
    ))

    print(process_and_insert_table(
        dr=dr,
        team_name='T',
        tag_name='bat',
        table_name='bat_balls_table',
        sheet_name='batting',
        start_cell='T30',
        delay=2
    ))


    print(process_and_insert_table(
        dr=dr,
        team_name='T',
        tag_name='bat',
        table_name='bat_score_table',
        sheet_name='batting',
        start_cell='AN30',
        delay=2
    ))

    print(process_and_insert_table(
        dr=dr,
        team_name='W',
        tag_name='bat',
        table_name='bat_atk_table',
        sheet_name='batting',
        start_cell='A61',
        delay=2
    ))


    print(process_and_insert_table(
        dr=dr,
        team_name='W',
        tag_name='bat',
        table_name='bat_balls_table',
        sheet_name='batting',
        start_cell='T61',
        delay=2
    ))


    print(process_and_insert_table(
        dr=dr,
        team_name='W',
        tag_name='bat',
        table_name='bat_score_table',
        sheet_name='batting',
        start_cell='AN61',
        delay=2
    ))

    print(process_and_insert_table(
        dr=dr,
        team_name='G',
        tag_name='bat',
        table_name='bat_atk_table',
        sheet_name='batting',
        start_cell='A89',
        delay=2
    ))


    print(process_and_insert_table(
        dr=dr,
        team_name='G',
        tag_name='bat',
        table_name='bat_balls_table',
        sheet_name='batting',
        start_cell='T88',
        delay=2
    ))


    print(process_and_insert_table(
        dr=dr,
        team_name='G',
        tag_name='bat',
        table_name='bat_score_table',
        sheet_name='batting',
        start_cell='AN88',
        delay=2
    ))

    print(process_and_insert_table(
        dr=dr,
        team_name='R',
        tag_name='bat',
        table_name='bat_atk_table',
        sheet_name='batting',
        start_cell='A122',
        delay=2
    ))


    print(process_and_insert_table(
        dr=dr,
        team_name='R',
        tag_name='bat',
        table_name='bat_balls_table',
        sheet_name='batting',
        start_cell='T121',
        delay=2
    ))


    print(process_and_insert_table(
        dr=dr,
        team_name='R',
        tag_name='bat',
        table_name='bat_score_table',
        sheet_name='batting',
        start_cell='AN121',
        delay=2
    ))

    print(process_and_insert_table(
        dr=dr,
        team_name='UL',
        tag_name='bat',
        table_name='bat_atk_table',
        sheet_name='batting',
        start_cell='A152',
        delay=2
    ))


    print(process_and_insert_table(
        dr=dr,
        team_name='UL',
        tag_name='bat',
        table_name='bat_balls_table',
        sheet_name='batting',
        start_cell='T151',
        delay=2
    ))


    print(process_and_insert_table(
        dr=dr,
        team_name='UL',
        tag_name='bat',
        table_name='bat_score_table',
        sheet_name='batting',
        start_cell='AN151',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='B',
        tag_name='pitch',
        table_name='pitch_data_table',
        sheet_name='pitching',
        start_cell='A1',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='B',
        tag_name='pitch',
        table_name='pitch_content_table',
        sheet_name='pitching',
        start_cell='V1',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='B',
        tag_name='pitch',
        table_name='pitch_score_table',
        sheet_name='pitching',
        start_cell='AN1',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='T',
        tag_name='pitch',
        table_name='pitch_data_table',
        sheet_name='pitching',
        start_cell='A33',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='T',
        tag_name='pitch',
        table_name='pitch_content_table',
        sheet_name='pitching',
        start_cell='V33',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='T',
        tag_name='pitch',
        table_name='pitch_score_table',
        sheet_name='pitching',
        start_cell='AN33',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='W',
        tag_name='pitch',
        table_name='pitch_data_table',
        sheet_name='pitching',
        start_cell='A61',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='W',
        tag_name='pitch',
        table_name='pitch_content_table',
        sheet_name='pitching',
        start_cell='V61',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='W',
        tag_name='pitch',
        table_name='pitch_score_table',
        sheet_name='pitching',
        start_cell='AN61',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='G',
        tag_name='pitch',
        table_name='pitch_data_table',
        sheet_name='pitching',
        start_cell='A89',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='G',
        tag_name='pitch',
        table_name='pitch_content_table',
        sheet_name='pitching',
        start_cell='V89',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='G',
        tag_name='pitch',
        table_name='pitch_score_table',
        sheet_name='pitching',
        start_cell='AN89',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='R',
        tag_name='pitch',
        table_name='pitch_data_table',
        sheet_name='pitching',
        start_cell='A118',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='R',
        tag_name='pitch',
        table_name='pitch_content_table',
        sheet_name='pitching',
        start_cell='V118',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='R',
        tag_name='pitch',
        table_name='pitch_score_table',
        sheet_name='pitching',
        start_cell='AN118',
        delay=2
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='UL',
        tag_name='pitch',
        table_name='pitch_data_table',
        sheet_name='pitching',
        start_cell='A145',
        delay=3
    ))
    print(process_and_insert_table(
        dr=dr,
        team_name='UL',
        tag_name='pitch',
        table_name='pitch_content_table',
        sheet_name='pitching',
        start_cell='V145',
        delay=3
    ))
print(process_and_insert_table(
        dr=dr,
        team_name='UL',
        tag_name='pitch',
        table_name='pitch_score_table',
        sheet_name='pitching',
        start_cell='AN145',
        delay=3
    ))



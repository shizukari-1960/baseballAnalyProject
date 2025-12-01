import os

import gsheet
import selen

#print(selen.get_table(dr= selen.webdrive_init(), team_name='T', tag_name='pitch', table_name='pitch_score_table'))

os.chdir(os.path.dirname(os.path.abspath(__file__)))
def formatize():
    pass

gsheet.insert_matrix(sheet_name='worksheet1',start_cell='A1',data_list=[[1,2,3]])

#TODO: assign data range from url = 'https://www.rebas.tw/tournament/CPBL-2025-JO/firstbase/full'
teams_alias = ['league','CTBC','TSGH', 'WCG', 'FBG', 'RKMK', 'UNL']
tags = ['bat', 'pitch']
button_tables_storage = {
    
    'league': {
        'button': '//*[@id="app-content"]/div/div[1]/div[2]/div[8]/a[1]/button',
        #---------------------------bat area---------------------------
        'bat' : '//*[@id="app-content"]/div/div[2]/div[1]', #tag button

        'league_bat_atk_sumup_table' : '//*[@id="app-content"]/div/div[3]/div[2]/div/table[1]',
        'team_bat_atk_sumup_table' : '//*[@id="app-content"]/div/div[3]/div[2]/div/table[2]',

        'league_bat_balls_sumup_table' : '//*[@id="app-content"]/div/div[3]/div[5]/div/table[1]',
        'team_bat_balls_sumup_table' : '//*[@id="app-content"]/div/div[3]/div[5]/div/table[2]',

        'league_bat_score_sumup_table' : '//*[@id="app-content"]/div/div[3]/div[8]/div/table[1]',
        'team_bat_score_sumup_table' : '//*[@id="app-content"]/div/div[3]/div[8]/div/table[2]',
        #---------------------------pitch area---------------------------
        'pitch' : '//*[@id="app-content"]/div/div[2]/div[2]', #tag button

        'league_pitch_sumup_table' : '//*[@id="app-content"]/div/div[3]/div[2]/div/table[1]',
        'team_pitch_sumup_table': '//*[@id="app-content"]/div/div[3]/div[2]/div/table[2]',

        'league_pitch_content_sumup_table': '//*[@id="app-content"]/div/div[3]/div[5]/div/table[1]',
        'team_pitch_content_sumup_table': '//*[@id="app-content"]/div/div[3]/div[5]/div/table[2]',

        'league_pitch_score_sumup_table': '//*[@id="app-content"]/div/div[3]/div[8]/div/table[1]',
        'team_pitch_score_sumup_table' : '//*[@id="app-content"]/div/div[3]/div[8]/div/table[2]'     
    },
    'CTBC':{
        'button': '//*[@id="app-content"]/div/div[1]/div[2]/div[8]/a[2]/button',
        #---------------------------bat area---------------------------
        'bat': '//*[@id="app-content"]/div/div[2]/div[1]',
        
        'bat_atk_table': '//*[@id="app-content"]/div/div[3]/div[8]/div/table[2]',
        'bat_balls_table': '//*[@id="app-content"]/div/div[3]/div[11]/div/table[2]',
        'bat_score_table': '//*[@id="app-content"]/div/div[3]/div[14]/div/table[2]',

    }
}
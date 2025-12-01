teams_alias = ['league','B','T', 'W', 'G', 'R', 'UL']
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
    'B':{
        'button': '//*[@id="app-content"]/div/div[1]/div[2]/div[8]/a[2]/button'
    },
    'T':{
        'button': '//*[@id="app-content"]/div/div[1]/div[2]/div[8]/a[3]/button'
    },
    'W':{
        'button': '//*[@id="app-content"]/div/div[1]/div[2]/div[8]/a[4]/button'
    },
    'G':{
        'button': '//*[@id="app-content"]/div/div[1]/div[2]/div[8]/a[5]/button'
    },
    'R':{
        'button': '//*[@id="app-content"]/div/div[1]/div[2]/div[8]/a[6]/button'
    },
    'UL':{
        'button': '//*[@id="app-content"]/div/div[1]/div[2]/div[8]/a[7]/button'
    }, #sacrifice for main readbility.
    'team':{
        #---------------------------bat area---------------------------
        'bat': '//*[@id="app-content"]/div/div[2]/div[1]',
        
        'bat_atk_table': '//*[@id="app-content"]/div/div[3]/div[8]/div/table[2]',
        'bat_balls_table': '//*[@id="app-content"]/div/div[3]/div[11]/div/table[2]',
        'bat_score_table': '//*[@id="app-content"]/div/div[3]/div[14]/div/table[2]',
        #---------------------------pitch area---------------------------
        'pitch': '//*[@id="app-content"]/div/div[2]/div[2]',

        'pitch_data_table': '//*[@id="app-content"]/div/div[3]/div[8]/div[1]/table[2]',
        'pitch_content_table': '//*[@id="app-content"]/div/div[3]/div[11]/div[1]/table[2]',
        'pitch_score_table': '//*[@id="app-content"]/div/div[3]/div[14]/div[1]/table[2]'
    }
}
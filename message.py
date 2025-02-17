import codeforces_data as codeforces
import atcoder_data as atcoder

space = '        '

def get_contest_list(type, list):
    if list == []:
        return f'### 아직 예정된 {type} 대회가 없습니다 :cry:'
        
    title = f'## :pushpin: {type} 대회 일정'
    table_header = '```날짜          시작         대회'
    message = f'{title}\n{table_header}'
    
    for contest in list:
        message += f'\n{contest['date']}{space}{contest['start']}{space}{contest['name']}'
        
    message += '```'
    
    return message

def get_message(type):
    if type == 'codeforces':
        return get_contest_list('코드포스', codeforces.before_contest_list)
    elif type == 'atcoder':
        return get_contest_list('앳코더', atcoder.before_contest_list)
    elif type == 'all':
        return get_contest_list('코드포스 및 앳코더', codeforces.before_contest_list + atcoder.before_contest_list)
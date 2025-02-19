import codeforces_data as codeforces
import atcoder_data as atcoder

def get_grouped_list(contest_list):
    contest_dict = {}
    for date, start, name in contest_list:
        if date in contest_dict:
            contest_dict[date].append([start, name])
        else:
            contest_dict[date] = [[start, name]]
            
    grouped_list = [[key, value] for key, value in contest_dict.items()]
    grouped_list.sort()
    
    return grouped_list

def get_contest_list(type, list):
    if list == []:
        return f'### 아직 예정된 {type} 대회가 없습니다 :cry:'
        
    message = f'## :pushpin: {type} 대회 일정\n'
    
    for date, group in list:
        message += f'**{date}**\n'
        for start, name in group:
            message += f'> [{start}] {name}\n'
    
    return message

def get_message(type):
    codeforces_list = get_grouped_list(codeforces.before_contest_list)
    atcoder_list = get_grouped_list(atcoder.before_contest_list)
    all_list = get_grouped_list(codeforces.before_contest_list + atcoder.before_contest_list)
    
    if type == 'codeforces':
        return get_contest_list('코드포스', codeforces_list)
    elif type == 'atcoder':
        return get_contest_list('앳코더', atcoder_list)
    elif type == 'all':
        return get_contest_list('코드포스 및 앳코더', all_list)
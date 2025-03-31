import codeforces_data as codeforces
import atcoder_data as atcoder
from datetime import datetime
import setting

def get_grouped_list(contest_list): # contest_list를 같은 날짜끼리 묶어서 반환
    contest_dict = {}
    for date, start, name, type in contest_list:
        if date in contest_dict:
            contest_dict[date].append([start, name, type])
        else:
            contest_dict[date] = [[start, name, type]]
            
    grouped_list = [[key, value] for key, value in contest_dict.items()]
    grouped_list.sort()
    
    return grouped_list

def convert_time(time): #00-00을 오전/오후 00시 00분으로 반환
    hour = int(time[0:2])
    minute = int(time[3:])
    txt_time = ''
    
    if hour > 12:
        hour -= 12
        txt_time += '오후 '
    else:
        txt_time += '오전 '
        
    txt_time += f'{hour}시'
    
    if minute != 0:
        txt_time += f' {minute}분'
    
    return txt_time

def get_all_icon(contest_type): # 대회 종류 따라 앞에 들어갈 글자 반환
    if contest_type == 'codeforces':
        return setting.codeforces_icon
    else:
        return setting.atcoder_icon

def get_command_message(command_type, list): # 전체 대회 일정 반환
    if list == []:
        return f'### 아직 예정된 {command_type} 대회가 없습니다 :cry:'
        
    message = f'## :pushpin: {command_type} 대회 일정\n'
    
    for date, group in list:
        message += f'**{date}**\n'
        for start, name, type in group:
            message += '> '
            if command_type == '코드포스 및 앳코더':
                message += f'{get_all_icon(type)} '
            message += f'[{start}] {name}\n'
    
    return message

def get_daily_message_list(all_list): # 그날 대회 일정을 list로 반환
    today = datetime.today().strftime('%m-%d')
    today_group = []
    for date, group in all_list:
        if date == today:
            today_group = group
            break
    
    message_list = []
    for contest in today_group:
        contest_type = ''
        if contest[2] == 'codeforces':
            contest_type = '코드포스'
        else:
            contest_type = '앳코더'
            
        message = ''
        if contest_type == '코드포스':
            message += f'# <:codeforces:{setting.codeforces_emoji_id}> {contest[1]}\n'
            message += f'오늘 **{convert_time(contest[0])}**에 {contest_type}에서 [**{contest[1]}**](https://codeforces.com/contests)가 열립니다. 많은 참여 부탁드립니다!'
        else:
            message += f'# <:atcoder:{setting.atcoder_emoji_id}> {contest[1]}\n'
            message += f'오늘 **{convert_time(contest[0])}**에 {contest_type}에서 [**{contest[1]}**](https://atcoder.jp/contests/)가 열립니다. 많은 참여 부탁드립니다!'
            
        message_list.append(message)
        
    return message_list

def get_message_by_type(type):
    codeforces_list = get_grouped_list(codeforces.before_contest_list)
    atcoder_list = get_grouped_list(atcoder.before_contest_list)
    all_list = get_grouped_list(codeforces.before_contest_list + atcoder.before_contest_list)
    
    if type == 'codeforces':
        return get_command_message('코드포스', codeforces_list)
    elif type == 'atcoder':
        return get_command_message('앳코더', atcoder_list)
    elif type == 'all':
        return get_command_message('코드포스 및 앳코더', all_list)
    else:
        return get_daily_message_list(all_list)
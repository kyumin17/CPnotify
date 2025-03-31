import requests
import datetime

before_contest_list = []

def get_time(timestamp):
    kst = datetime.timezone(datetime.timedelta(hours=9))
    kst_time = str(datetime.datetime.fromtimestamp(timestamp, tz=kst))
    
    return kst_time

def get_data():
    global before_contest_list
    
    # api 호출
    update_list = []
    response = requests.get('https://codeforces.com/api/contest.list')
    if response.status_code == 200:
        contest_list = response.json()['result']
        filter_list = [contest for contest in contest_list if contest['phase'] == 'BEFORE']
        
        for contest in filter_list:
            timezone = get_time(contest['startTimeSeconds'])
            date = timezone[5:10]
            start = timezone[11:16]
            name = contest['name']
            
            if 'Div' in name:
                update_list.append([date, start, name, 'codeforces'])
    else:
        print('codeforces data loading error: ' + response.status_code)
    
    before_contest_list = update_list
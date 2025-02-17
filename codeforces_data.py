import requests
import datetime
import schedule

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
            start_time = get_time(contest['startTimeSeconds'])
            update_list.append({'date': start_time[5:10], 'start': start_time[11:16], 'name': contest['name']})
            
    before_contest_list = update_list

get_data()
schedule.every().day.at("06:00").do(get_data) # 6시마다 데이터 가져옴
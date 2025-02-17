import requests
from bs4 import BeautifulSoup
import re
import schedule

before_contest_list = []

def get_data():
    global before_contest_list
    
    # 세팅
    update_list = []
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    })

    url = 'https://atcoder.jp/contests/'
    response = session.get(url)

    # 크롤링
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        contest_table = soup.select_one('div#contest-table-upcoming')
        contest_list = contest_table.select('div > div > table > tbody > tr')
        
        for contest in contest_list:
            row = re.sub('<.+?>', '', str(contest), 0).strip().split('\n')
            update_list.append({'date' : row[0][5:10], 'start': row[0][11:16] ,'name': row[4], 'duration': row[6], 'rating': row[7]})
    
    before_contest_list = update_list

get_data()
schedule.every().day.at("06:00").do(get_data) # 6시마다 데이터 가져옴
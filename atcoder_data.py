import requests
from bs4 import BeautifulSoup
import re

before_contest_list = []

def get_data():
    global before_contest_list
    
    # 세팅
    update_list = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': 'no-cache',
    }
    
    url = 'https://atcoder.jp/contests/'
    response = requests.get(url, headers=headers)

    # 크롤링
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        contest_table = soup.select_one('div#contest-table-upcoming')
        contest_list = contest_table.select('div > div > table > tbody > tr')
        
        for contest in contest_list:
            data = re.sub('<.+?>', '', str(contest), 0).strip().split('\n')
            date = data[0][5:10]
            start = data[0][11:16]
            name = data[4]
            
            update_list.append([date, start, name, 'atcoder'])
    else:
        print('atcoder data loading error: ' + str(response.status_code))
    
    before_contest_list = update_list
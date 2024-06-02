# web_scraping.py

# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def web_scraping():
    url = 'https://example-news-site.com'  # 任意のニュースサイトのURLを指定
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # ニュース記事のタイトルを抽出（ここでは例としてh2タグを使用）
        titles = soup.find_all('h2', class_='article-title')
        print('最新の記事タイトル:')
        for title in titles:
            print(title.get_text())
    else:
        print(f'リクエストが失敗しました。ステータスコード: {response.status_code}')

web_scraping()

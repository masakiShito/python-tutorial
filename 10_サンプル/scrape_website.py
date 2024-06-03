import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    指定したURLのウェブサイトをスクレイピングする。

    Parameters:
    - url: スクレイピングするウェブサイトのURL
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 例として、すべての見出しを取得する
    headings = soup.find_all('h2')
    for heading in headings:
        print(heading.get_text())

if __name__ == "__main__":
    website_url = "https://example.com"  # ここにスクレイピングするウェブサイトのURLを入力してください

    scrape_website(website_url)

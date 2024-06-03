import requests

def get_weather(api_key, city):
    """
    指定した都市の天気情報を取得する。

    Parameters:
    - api_key: OpenWeatherMap APIキー
    - city: 天気情報を取得する都市名
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"都市: {data['name']}")
        print(f"天気: {data['weather'][0]['description']}")
        print(f"気温: {data['main']['temp']}°C")
        print(f"湿度: {data['main']['humidity']}%")
    else:
        print(f"天気情報を取得できませんでした: {data['message']}")

if __name__ == "__main__":
    api_key = "your_openweathermap_api_key"  # ここにOpenWeatherMapのAPIキーを入力してください
    city_name = "Tokyo"

    get_weather(api_key, city_name)

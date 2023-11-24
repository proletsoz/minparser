import requests
from bs4 import BeautifulSoup

url = 'ваш_сайт'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # Извлекаем заголовки, например, используя тег h1
    headers = soup.find_all('h1')

    for header in headers:
        print(header.text)
else:
    print(f"Ошибка при получении страницы. Код статуса: {response.status_code}")
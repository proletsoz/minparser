from bs4 import BeautifulSoup
import requests

def parse_pages(urls, output_file='output.html'):
    with open(output_file, 'w', encoding='utf-8') as file:
        for url in urls:
            # Отправка запроса на сервер и получение HTML-кода страницы
            response = requests.get(url)
            html = response.text

            # Создание объекта BeautifulSoup для парсинга HTML
            soup = BeautifulSoup(html, 'html.parser')

            # Извлечение всех таблиц на странице
            tables = soup.find_all('table', class_='grid')

            # Запись таблиц в файл
            for table in tables:
                file.write(str(table.prettify()))
                file.write('\n\n')
                
# Пример использования с несколькими страницами
urls_to_parse = [
    'https://index.minfin.com.ua/tariff/electric/',
    'https://index.minfin.com.ua/tariff/gas/',
    # Добавьте дополнительные URL-ы, если необходимо
]

parse_pages(urls_to_parse)

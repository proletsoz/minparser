from bs4 import BeautifulSoup
import requests
import time


def parse_pages(urls, output_file='readme.md'):
    with open(output_file, 'w', encoding='utf-8') as file:

        # Запись времени срабатывания скрипта
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file.write(f"# Скрипт сработал: {current_time}\n\n")

        # file.write(
        #     '<link rel="stylesheet" type="text/css" href="styles.css">\n\n')

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


# Пример использования с несколькими страницами
urls_to_parse = [
    'https://index.minfin.com.ua/tariff/electric/',
    'https://index.minfin.com.ua/tariff/gas/',
    # Добавьте дополнительные URL-ы, если необходимо
]

parse_pages(urls_to_parse)

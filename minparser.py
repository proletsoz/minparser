from bs4 import BeautifulSoup
import requests
import time


def parse_pages(urls, output_file='README.md'):
    with open(output_file, 'w', encoding='utf-8') as file:
        # Запись заголовка
        file.write('# Тарифы и индексы\n\n')

        for url in urls:
            # Отправка запроса на сервер и получение HTML-кода страницы
            response = requests.get(url)
            html = response.text

            # Создание объекта BeautifulSoup для парсинга HTML
            soup = BeautifulSoup(html, 'html.parser')

            # Извлечение всех таблиц на странице
            tables = soup.find_all('table', class_='grid')

            # Запись заголовка для каждой страницы
            file.write(f'## {url}\n\n')

            # Запись таблиц в файл в формате Markdown
            for table in tables:
                # Извлечение строк и столбцов таблицы
                rows = table.find_all('tr')
                for row in rows:
                    columns = row.find_all(['td', 'th'])
                    column_texts = [column.get_text(
                        strip=True) for column in columns]
                    file.write('|'.join(column_texts) + '\n')
                file.write('\n')

            # Запись времени срабатывания скрипта
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            file.write(f"Скрипт сработал в: {current_time}\n\n")


# Пример использования с несколькими страницами
urls_to_parse = [
    'https://index.minfin.com.ua/tariff/electric/',
    'https://index.minfin.com.ua/tariff/gas/',
    # Добавьте дополнительные URL-ы, если необходимо
]

parse_pages(urls_to_parse)

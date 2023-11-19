from bs4 import BeautifulSoup
import requests


def parse_table_contents(urls, output_file='readme.md'):
    with open(output_file, 'w', encoding='utf-8') as file:
        for url in urls:
            # Отправка запроса на сервер и получение HTML-кода страницы
            response = requests.get(url)
            html = response.text

            # Создание объекта BeautifulSoup для парсинга HTML
            soup = BeautifulSoup(html, 'html.parser')

            # Извлечение всех таблиц на странице
            tables = soup.find_all('table', class_='grid')

            # Парсинг содержимого каждой таблицы и запись в файл
            for table in tables:
                # Извлечение текста из тега <caption> (если есть) и удаление тега из дерева разбора
                caption = table.find('caption')
                caption_text = '## ' + \
                    caption.get_text(strip=True) if caption else ''
                if caption:
                    caption.extract()

                # Извлечение текста из таблицы в формате Markdown
                table_text = ''
                for row in table.find_all('tr'):
                    columns = row.find_all(['th', 'td'])
                    row_text = '|'.join([column.get_text(strip=True)
                                        for column in columns])
                    table_text += f"{row_text}|\n"

                # Запись текста из тега <caption> и текста таблицы в файл
                file.write(caption_text)
                file.write('\n\n' + table_text)
                # Добавляем разделитель между таблицами
                file.write('\n\n' + '-'*20 + '\n\n')


# Пример использования
urls_to_parse = [
    'https://index.minfin.com.ua/tariff/electric/',
    'https://index.minfin.com.ua/tariff/gas/',
    # Добавьте дополнительные URL-ы, если необходимо
]

parse_table_contents(urls_to_parse)

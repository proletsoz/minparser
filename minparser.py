from bs4 import BeautifulSoup
import requests
import time


def parse_pages(urls, output_file='readme.md'):
    with open(output_file, 'w', encoding='utf-8') as file:
        # Запись времени срабатывания скрипта
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file.write(f"# Скрипт сработал: {current_time}\n\n")

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
                # Извлечение заголовка таблицы и удаление тега <caption>
                table_caption = table.find('caption')
                if table_caption:
                    caption_text = table_caption.text
                    table_caption.decompose()
                else:
                    caption_text = ''

                # Запись текста заголовка с добавлением "##"
                file.write(f"## {caption_text}\n\n")

                # Добавление стилей для уменьшения размера шрифта
                table_style = 'font-size: 0.8em;'  # Попробуйте разные значения
                table['style'] = table_style

                # Запись таблицы без тега <caption>
                file.write(str(table.prettify()))
                file.write('\n\n')


# Пример использования с несколькими страницами
urls_to_parse = [
    'https://index.minfin.com.ua/tariff/electric/',
    'https://index.minfin.com.ua/tariff/gas/',
    # Добавьте дополнительные URL-ы, если необходимо
]

parse_pages(urls_to_parse)

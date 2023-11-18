from bs4 import BeautifulSoup
import requests

def parse_pages(urls, keywords, output_file='output.txt'):
    with open(output_file, 'w', encoding='utf-8') as file:
        for url in urls:
            # Отправка запроса на сервер и получение HTML-кода страницы
            response = requests.get(url)
            html = response.text

            # Создание объекта BeautifulSoup для парсинга HTML
            soup = BeautifulSoup(html, 'html.parser')

            # Извлечение всех параграфов со страницы
            paragraphs = soup.find_all('p')

            # Извлечение элемента <div class="idx-updatetime">
            update_time_element = soup.find('div', class_='idx-updatetime')
            update_time_text = update_time_element.text.strip()

            # Запись информации о времени обновления в файл
            file.write(f"URL: {url}\n")
            file.write(f"Последнее обновление: {update_time_text}\n\n")

            # Поиск и запись параграфов, содержащих ключевые слова, в файл
            for paragraph in paragraphs:
                for keyword in keywords:
                    if keyword.lower() in paragraph.text.lower():
                        file.write(paragraph.text + '\n')
                        break
            # Пробел
            file.write('\n')

# Пример использования с несколькими страницами
urls_to_parse = [
    'https://index.minfin.com.ua/economy/index/inflation/',
    'https://index.minfin.com.ua/economy/index/industrial/',
    'https://index.minfin.com.ua/economy/index/agroprice/',
    'https://index.minfin.com.ua/economy/index/buildprice/',
    # Добавьте дополнительные URL-ы, если необходимо
]
search_keywords = ['Индекс инфляции в Украине', 
                   'Базовый индекс инфляции', 
                   'Индекс промпроизводства в Украине',
                   'Индекс цен агропродукции в Украине',
                   'Индекс цен строительства в Украине',
                   ]

parse_pages(urls_to_parse, search_keywords)
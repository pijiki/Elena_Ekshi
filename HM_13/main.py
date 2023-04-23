from configs import *
from base_parser import BaseParser
from mixin import ProductDetailMixin
import time

from bs4 import BeautifulSoup


class CategoryParser(BaseParser, ProductDetailMixin):
    def __init__(self):
        super(CategoryParser, self).__init__()
        self.DATA = {}

    def category_block_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        category_links = soup.find_all('a', class_='category__link')
        for category in category_links[:15]:
            category_title = category.find(
                'h2', class_='content__title').get_text(strip=True)
            self.DATA[category_title] = []
            category_link = self.host + category.get('href')
            category_page = self.get_html(category_link)
            self.category_page_parser(category_page, category_title)

    def category_page_parser(self, category_page, category_title):
        soup = BeautifulSoup(category_page, 'html.parser')
        section = soup.find('div', class_='catalog-content__products')
        products = section.find_all('div', class_='product-item-wrapper')
        for product in products[:3]:
            product_name = product.find('a', class_='product-name').get_text(
                strip=True)
            product_price = product.find('div', class_='f-16').get_text(
                strip=True)
            product_link = self.host + product.find('a',
                                                    class_='product-link').get(
                'href')
            product_detail_page = self.get_html(product_link)
            characteristics = self.get_detail_info(product_detail_page)
            self.DATA[category_title].append({
                "Имя продукта": product_name,
                "Цена продукта": product_price,
                "Ссылка на продукт": product_link,
                "Характеристики": characteristics
            })

        time.sleep(5)


def start_category_parsing():
    parser = CategoryParser()
    # category = input('Введите категорию: ')  # telefony
    category = 'telefony'
    category_link = 'https://texnomart.uz/ru/katalog/' + category

    print(Color.RED + 'Парсер начал работу')
    start = time.time()
    html = parser.get_html(category_link)
    parser.category_block_parser(html)
    parser.save_data_to_json(category, parser.DATA)

    finish = time.time()
    print(
        Color.GREEN + f'Парсер завершил работу за {round(finish - start), 2} cекунд')


start_category_parsing()

from bs4 import BeautifulSoup
import re


class ProductDetailMixin:
    def get_detail_info(self, page):
        characteristics = {}
        soup = BeautifulSoup(page, 'html.parser')
        sections = soup.find_all('div', class_='characteristic-item')
        for section in sections:
            try:
                title = section.find('div', class_='title').get_text(
                    strip=True)
                list_items = section.find_all('div', class_='list__item')
                characteristics[title] = {
                    re.match("^[А-Я][а-я ]+", i.find('div', class_='list__name').get_text(strip=True)).group():
                        i.find('div', class_='list__value').get_text(strip=True) for i in list_items
                }
            except Exception as e:
                print(e)

        return characteristics

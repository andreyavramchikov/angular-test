import time

from django.core.management.base import BaseCommand

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from shop.management.utils import _get_firefox_profile
from shop.models import Category, Product

driver = webdriver.Firefox(firefox_profile=_get_firefox_profile())


# python manage.py parse_reebok_products
class Command(BaseCommand):
    ROOT_URL = 'http://global.reebok.com/'
    ROOT_SUBCATEGORIES = ('kids', 'classics', 'women?grid=true', 'men?grid=true', 'sport')

    def handle(self, *args, **options):
        driver.get(self.ROOT_URL)
        for category in self.ROOT_SUBCATEGORIES:

            driver.get(self.ROOT_URL + category)

            try:
                top_pagesize = driver.find_element_by_id('top-pagesize')
                links = top_pagesize.find_elements_by_tag_name('a')
                links[len(links) - 1].click()
            except NoSuchElementException:
                pass
            time.sleep(5)
            try:
                pagination = driver.find_element_by_class_name('paging-select-wrapper')
            except NoSuchElementException:
                pagination = None

            if pagination:
                select_button = _get_select_button()
                select_button.click()
                time.sleep(5)
                for i in range(0, len(_get_lis())):
                    time.sleep(15)
                    _get_lis()[i].click()
                    time.sleep(10)

                    # find product fields
                    write_products_to_db()
                    _get_select_button().click()
            else:
                write_products_to_db()

        driver.close()


def write_products_to_db():
    products = _get_products()
    time.sleep(5)
    for product in products:
        name = product.find_element_by_class_name('title').text
        image_url = product.find_element_by_class_name('image').find_element_by_tag_name(
            'img').get_attribute('data-original')
        category = product.find_element_by_class_name('subtitle').text
        Category.objects.get_or_create(name=category)
        Product.objects.get_or_create(name=name, image_url=image_url, category=Category.objects.get(name=category))


def _get_products():
    container = driver.find_element_by_id('hc-container')
    products = container.find_elements_by_class_name('hockeycard')
    return products


def _get_lis():
    return _get_pagination().find_element_by_class_name(
        'ffSelectMenuMid').find_elements_by_tag_name('li')


def _get_select_button():
    return _get_pagination().find_element_by_class_name('ffSelectButton')


def _get_pagination():
    return driver.find_element_by_class_name('paging-select-wrapper')

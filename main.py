from selenium import webdriver

from locators import Locators

BASE_URL = "https://market.yandex.ru/catalog--lampochki/55150/list?"


def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    return options


def firefox_options():
    options = webdriver.FirefoxOptions()
    options.add_argument('--start-maximized')
    return options


def get_all_elements():
    return wd.find_elements_by_css_selector(Locators.SNIPPET_CELL)


def get_name_product():
    return get_all_elements()[0].find_element_by_css_selector(Locators.TITLE).text


def get_price_product():
    return get_all_elements()[0].find_element_by_css_selector(Locators.PRICE).text


def get_href_product():
    return get_all_elements()[0].find_element_by_css_selector(Locators.HREF).get_attribute("href")


def get_lowest_price():
    wd.get(BASE_URL + "how=aprice&viewtype=grid")
    print(f"""
    Product with lowest price is {str(get_name_product())}
    Price is {str(get_price_product())}
    You can buy it in by link: {str(get_href_product())}""")


def get_highest_price():
    wd.get(BASE_URL + "how=dprice&viewtype=grid")
    print(f"""
    Product with highest price is {str(get_name_product())}
    Price is {str(get_price_product())}
    You can buy it in by link: {str(get_href_product())}""")


wd = webdriver.Chrome("tools/chromedriver.exe", options=chrome_options())
wd.implicitly_wait(10)

if __name__ == '__main__':
    get_lowest_price()
    get_highest_price()

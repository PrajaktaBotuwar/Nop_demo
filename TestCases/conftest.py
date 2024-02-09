import pytest
from selenium import webdriver
# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     driver.get("https://admin-demo.nopcommerce.com/")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     return driver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


# we need to add command liner --browser
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Test Run - Browser Chrome")
        driver = webdriver.Chrome()
        driver.get("https://admin-demo.nopcommerce.com/")
    elif browser == "firefox":
        print("Test Run - Browser Firefox")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Test Run - Browser Edge")
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
        print("Test Run - Browser Headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.implicitly_wait(5)
    yield driver
#     driver.quit()


# @pytest.fixture(params=[
#     ("admin@yourstore.com", "admin", "Pass"),
#     ("admin@yourstore.com1", "admin", "Fail"),
#     ("admin@yourstore.com", "admin1", "Pass"),
#     ("admin@yourstore.com1", "admin1", "Fail")
# ])
# def DataForLogin(request):
#     return request.param

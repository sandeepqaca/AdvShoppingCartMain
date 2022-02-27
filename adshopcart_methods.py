import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\Sandeep Kaur\PycharmProjects\moodle2\chromedriver.exe')

def setUp():
    print(f'Test started at: {datetime.datetime.now()}')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.adShopCart_url)
    if driver.current_url == locators.adShopCart_url and driver.title.endswith('Advantage Shopping'):
        print(f'We\'re at {driver.current_url} homepage')
        print(f'Title message {driver.title} is visible')
    else:
        print(f'We\'re not at the {driver.current_url} homepage. Check your code!')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


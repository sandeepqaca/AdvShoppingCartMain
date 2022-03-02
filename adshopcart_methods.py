import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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


def register():
    if driver.current_url == locators.adShopCart_url:
        driver.find_element(By.ID, "menuUser").click()
        sleep(5)
        assert driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').is_displayed()
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(1)
        if driver.current_url == locators.create_user_url:
            assert driver.find_element(By.XPATH, '//h3[contains(.,"CREATE ACCOUNT")]').is_displayed()
            print(f'Create new user page is loaded successfully')
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, "[name='usernameRegisterPage']").send_keys(locators.username)
            driver.find_element(By.CSS_SELECTOR, "[name='emailRegisterPage']").send_keys(locators.email)
            driver.find_element(By.CSS_SELECTOR, "[name='passwordRegisterPage']").send_keys(locators.password)
            driver.find_element(By.CSS_SELECTOR, "[name='confirm_passwordRegisterPage']").send_keys(locators.password)
            driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
            driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
            driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone_number)
            driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys(locators.country)
            driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
            driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
            driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
            #driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
            sleep(1)
            driver.find_element(By.NAME, 'i_agree').click()
            driver.find_element(By.ID, 'register_btnundefined').click()
            sleep(0.5)
            if driver.find_element(By.ID, 'menuUser').is_displayed():
                print(f'User is created {locators.full_name} and {locators.email}')
                sleep(3)
            else:
                print(f'User is not created. Check your code')


def log_out():
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"Sign out")]').click()
    sleep(3)
    if driver.current_url == locators.adShopCart_url:
        print(f'User {locators.full_name}--{locators.email} Sign out')
        sleep(1)
    else:
        print(f'Error message')


def log_in():
    if driver.current_url == locators.adShopCart_url:
        driver.find_element(By.ID, "menuUser").click()
        sleep(0.25)
        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        print(f'User {locators.full_name}--{locators.email} logged in ')
        sleep(1)
    else:
        print(f'Error message')


def delete_user():
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//div[text()="yes"]').click()
    sleep(5)
    print(f'Account deleted for {locators.username}')
    sleep(5)


def login_with_deleted_cred():
    driver.find_element(By.ID, "menuUser").click()
    sleep(0.25)
    driver.find_element(By.NAME, 'username').send_keys(locators.username)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(1)
    if driver.find_element(By.ID, 'signInResultMessage'):
        print(f'Incorrect user name or password.')
    else:
        print(f'Account exist')


def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

setUp()
register()
log_out()
log_in()
delete_user()
login_with_deleted_cred()
tearDown()



import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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


def navigate_homepage():
    if driver.current_url == locators.adShopCart_url:
        assert driver.find_element(By.ID, 'speakersTxt').is_displayed()
        sleep(0.25)
        assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
        sleep(0.25)
        assert driver.find_element(By.ID, 'headphonesTxt').is_displayed()
        sleep(0.25)
        assert driver.find_element(By.ID, 'laptopsTxt').is_displayed()
        sleep(0.25)
        assert driver.find_element(By.ID, 'miceTxt').is_displayed()
        sleep(2)
        print(f'--Find great deals on SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE --')
        driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').click()
        print(f'-----OUR PRODUCTS Clicked-----')
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
        print(f'-----SPECIAL OFFER Clicked-----')
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
        print(f'-----POPULAR ITEMS Clicked-----')
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        print(f'-----CONTACT US Clicked-----')
        sleep(0.25)


def check_contact_us():
    if driver.current_url == locators.adShopCart_url:
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Laptops')
        sleep(1)
        Select(driver.find_element(By.XPATH, "//*[name='productListboxContactUs']")).select_by_visible_text('HP Chromebook 14 G1(ENERGY STAR)')
        sleep(1)
        driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
        driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.subject)
        driver.find_element(By.ID, 'send_btnundefined').click()
        print(f'Thank you for contacting Advantage support. Is displayed')


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
            driver.find_element(By.ID, "menuUser").click()
            sleep(1)
            driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
            sleep(0.25)
            print(f'{locators.full_name}')
            sleep(5)
            driver.find_element(By.ID, "menuUser").click()
            sleep(1)
            driver.find_element(By.XPATH, '//a/div/label[contains(.,"My orders")]').click()
            sleep(0.25)
            print(f'No Orders')
            sleep(5)


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

'''
setUp()
navigate_homepage()
check_contact_us()
register()
log_out()
log_in()
delete_user()
login_with_deleted_cred()
tearDown()
'''


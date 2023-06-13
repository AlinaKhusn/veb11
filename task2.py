from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains


sbis_fix = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()

try:
    driver.get(sbis_fix)
    sleep(2)
    user_login, user_password = 'чихнул', 'чихнул123'
    name = '67890 Иапа'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)
    new_message = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"] [data-qa="counter"]')
    message1 = new_message.text
    Contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    action = ActionChains(driver)
    action.double_click(Contacts).perform()
    sleep(3)
    Contacts2 = driver.find_element(By.CSS_SELECTOR, '.controls-BaseButton__wrapper')
    Contacts2.click()
    sleep(5)
    find = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate-content [name="ws-input_2023-06-13"]')
    find.send_keys('иапа', Keys.ENTER)
    sleep(5)
    name = driver.find_element(By.CSS_SELECTOR, '.msg-addressee-item')
    name.click()
    sleep(5)
    message = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    message.send_keys('Привет!', Keys.ENTER)
    sleep(3)
    send_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    sleep(5)
    send_btn.click()
    sleep(5)
    new_message = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"] [data-qa="counter"]')
    message2 = new_message.text
    assert int(message1) + 1 == int(message2)  # проверяем что поступило новое сообщение
    sleep(4)
    Contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    Contacts.click()
    sleep(3)
    Contacts3 = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    Contacts3.click()
    sleep(5)
    messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-detail__layout-content .controls-ListViewV .controls-ListView__itemV-relative')
    key = messages[0].get_attribute('attr-data-qa')
    my_message = driver.find_element(By.CSS_SELECTOR, f'[attr-data-qa = {key}]')
    my_message.click()
    sleep(5)
    removal = driver.find_element(By.CSS_SELECTOR, '[data-qa="remove"]')
    removal.click()
    sleep(5)
    messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-detail__layout-content .controls-ListViewV .controls-ListView__itemV-relative')
    assert messages[0].get_attribute('attr-data-qa') != key  #проверяем, что наше сообщение удалилось
finally:
    driver.quit()

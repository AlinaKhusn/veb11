from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

sbis = 'https://sbis.ru'
tensor_about = 'https://tensor.ru/about'
driver = webdriver.Chrome()
try:
    driver.get(sbis)
    Contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    Contacts.click()
    sleep(2)
    Tensor = driver.find_element(By.CSS_SELECTOR, '[id="contacts_clients"] [src="/resources/NewDesign/pages/Contacts/images/logo.svg?x_module=23.3206-53"]')
    Tensor.click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)
    sila = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    sila.location_once_scrolled_into_view
    assert sila.is_displayed()
    more = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    more.click()
    sleep(7)
    assert driver.current_url == tensor_about #роверяем, что перешли на https://tensor.ru/about'

finally:
    driver.quit()

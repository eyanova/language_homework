from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_incart_is_exists(browser):
    browser.get(link)
    time.sleep(7)
    a = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    print (len(a))
    assert len(a)==1, "Кнопка 'Добавить в корзину' не найдена!"



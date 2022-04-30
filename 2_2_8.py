import os
from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector('[placeholder="Enter first name"]').send_keys("Pavel")
    browser.find_element_by_css_selector('[placeholder="Enter last name"]').send_keys("Korchagin")
    browser.find_element_by_css_selector('[placeholder="Enter email"]').send_keys("p-korchagin@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_name = "file_example.txt"
    print(file_name)
    file_path = os.path.join(current_dir, file_name)
    print(file_path)
    element = browser.find_element_by_id('file')
    print(element)
    element.send_keys(file_path)
    
    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
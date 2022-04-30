from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена не снизится до $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    
    # Жмякаем на кнопку "Book"
    browser.find_element_by_id("book").click()
    
    # Цепляемся за поле х=... и прокручиваем вверх
    val = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", val)

    # Берем значение х=..., решаем задачу получаем y=...
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    
    # Вставляем знаачение y=... в поле ответ
    browser.find_element_by_id('answer').send_keys(y)
    
    # Жмякааем на кнопку "Submit"
    button = browser.find_element_by_id("solve").click()
    
    # Печатаем значение из окна Алерт.
    print(browser.switch_to.alert.text.split()[-1])

    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("button.btn").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    
    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    print(addToClipBoard)			# и число в буфере обмена


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
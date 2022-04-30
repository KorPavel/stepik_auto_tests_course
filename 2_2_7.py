import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_name = "file_example.txt"
print(file_name)
file_path = os.path.join(current_dir, file_name)
print(file_path)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
print(element)
element.send_keys(file_path)
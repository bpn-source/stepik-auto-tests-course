from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
try:
#    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")
    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)
    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x+y))
    button1 = browser.find_element_by_class_name("btn")
    button1.click()
finally:
    time.sleep(10)
    browser.quit()
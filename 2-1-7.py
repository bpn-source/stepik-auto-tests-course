from selenium import webdriver
import time, math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_tag_name("img")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    checkbox1 = browser.find_element_by_id("robotCheckbox")
    checkbox1.click()
    radio1 = browser.find_element_by_id("robotsRule")
    radio1.click()
    button1 = browser.find_element_by_class_name("btn")
    button1.click()
finally:
    time.sleep(10)
    browser.quit()
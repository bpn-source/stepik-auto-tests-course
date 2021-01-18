from selenium import webdriver
import time, math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id("answer").send_keys(y)
    checkbox1 = browser.find_element_by_id("robotCheckbox")
    checkbox1.click()
    radio1 = browser.find_element_by_id("robotsRule")
    radio1.click()
    button1 = browser.find_element_by_class_name("btn")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()
finally:
    time.sleep(10)
    browser.quit()
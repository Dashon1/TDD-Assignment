from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# initialize driver
opts = Options()
driver = webdriver.Chrome()

# open the app url
driver.get("https://sqa-310021.uc.r.appspot.com/")

# test values and see if we get a response
element = driver.find_element_by_id("feet")
element.send_keys("6")

element = driver.find_element_by_id("inches")
element.send_keys("6")

element = driver.find_element_by_id("weight")
element.send_keys("230")

element.send_keys(Keys.RETURN)

time.sleep(5)
driver.get("https://sqa-310021.uc.r.appspot.com/retirement")

# test values and see if we get a response
element = driver.find_element_by_id("age")
element.send_keys("23")

element = driver.find_element_by_id("salary")
element.send_keys("50000")

element = driver.find_element_by_id("saved")
element.send_keys("10")

element = driver.find_element_by_id("desired")
element.send_keys("1000000")

element.send_keys(Keys.RETURN)

# close browser
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path="C:/Users/SnappFood/.cache/selenium/chromedriver/win32/110.0.5481.77/chromedriver.exe")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
time.sleep(1)

message_field = driver.find_element(By.XPATH,'//*[@id="user-message"]')
message_field.send_keys("Hello Pedram")
time.sleep(1)

show_message_button = driver.find_element(By.XPATH,'//*[@id="get-input"]/button')
show_message_button.click()
time.sleep(1)

additional_field1 = driver.find_element(By.XPATH,'//*[@id="sum1"]')
additional_field1.send_keys("11")
time.sleep(1)
additional_field2 = driver.find_element(By.XPATH,'//*[@id="sum2"]')
additional_field2.send_keys("10")
time.sleep(1)

get_total_button = driver.find_element(By.XPATH,'//*[@id="gettotal"]/button')
get_total_button.click()

time.sleep(100)

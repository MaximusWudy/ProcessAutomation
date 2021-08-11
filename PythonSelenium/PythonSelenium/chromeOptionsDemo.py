import time

from selenium import webdriver
# from selenium.webdriver import ActionChains

'''
Chrome options class
* set up behavior of the browser when it's invoking
example website: https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") # open window as largest
chrome_options.add_argument("headless") # headless mode
chrome_options.add_argument("--ignore-certificate-errors") # ignore all cerfication asks

driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe', options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)

time.sleep(2)
driver.close()
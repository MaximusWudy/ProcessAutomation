'''
JS DOM can access any element on web page just like how selenium does
even more than selenium; selenium have a method to execute JS code in it
'''
import time

from selenium import webdriver
# from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text) # print blank
print(driver.find_element_by_name("name").get_attribute("value")) # value can also return text

# execute JS commands
print(driver.execute_script("return document.getElementsByName('name')[0].value"))

'''
JS Executer, when you have image hover over the click item, you cannot use selenium since it's not visible
However, you can use JS executer instead of depending on your frontend view
'''
shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)

# also selenium doesn't support scrolling down, need to use JS
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll to the end)

time.sleep(2)
driver.close()
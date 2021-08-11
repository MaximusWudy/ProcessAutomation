import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe')

'''
Mouse Hover
'''
driver.get("https://rahulshettyacademy.com/AutomationPractice")
# make advance interaction on top of your driver object on any browser
action = ActionChains(driver)
# you can have multiple chain of actions in an element, at the end execute by perform()
action.move_to_element(driver.find_element_by_css_selector("#mousehover")).perform()
action.move_to_element(driver.find_element_by_link_text("Top")).click().perform()

'''
Double Click
'''
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
# action chains
action = ActionChains(driver)
action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert # assign to an object
assert alert.text == "You double clicked me!!!, You got to be kidding me"
alert.accept()


time.sleep(2)
driver.close()
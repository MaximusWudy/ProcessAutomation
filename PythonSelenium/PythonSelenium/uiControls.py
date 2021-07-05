import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path='F:\\selenium\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']") # list of checkboxes

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected() # validation: tell whether the element is select (True/False)
        break
'''
radio button works the same as checkbox
'''
radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click() # select the 3rd one
assert radiobuttons[2].is_selected()

time.sleep(2)
driver.close()

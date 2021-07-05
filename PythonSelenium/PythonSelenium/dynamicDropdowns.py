'''
Practice website: https://rahulshettyacademy.com/dropdownsPractise/

'''
import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path='F:\\selenium\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.find_element_by_id('autosuggest').send_keys('ind')
time.sleep(2)

# no matter how many dynamic list returns, all stored here
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print("There are in total {} countries" .format(len(countries)))

for country in countries:
    if country.text == 'India':
        country.click() # click 'India' option and skip the rest
        break

time.sleep(2)

# selenium won't update with the dynamic page content change
assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India" # this will get value from DOM

driver.close()

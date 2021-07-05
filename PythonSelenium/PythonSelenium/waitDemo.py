# Implicit Wait - Global setting
# Explicit Wait
# pause the test for few seconds during execution

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path='F:\\selenium\chromedriver.exe')
# driver.implicitly_wait(5)
'''
# wait until 5 seconds if object is not displayed, globally applied
# Global wait
# 1.5 sec to reach next page -- resume immediately
# if object donot show up at all, then max time your test waits for 5 sec
'''
item_list_1 = []
item_list_2 = []

driver.get('https://rahulshettyacademy.com/seleniumPractise/')

# find element by CSS: tagname.classname
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)

product = driver.find_elements_by_xpath("//div[@class='products']/div")
print("Page returns {} products" .format(len(product)))

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    # ONLY xpath allow you to refer to parental elements, start searching from 'button'
    # //div[@class='product-action']/button/parent::div/parent::div/h4[@class='product-name']
    item_list_1.append(button.find_element_by_xpath("parent::div/parent::div/h4[@class='product-name']").text)
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
# explicit wait -- clearly telling that I want to wait until this element is present
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input.promoCode"))) # double bracket for arguments

veggies = driver.find_elements_by_css_selector("p.product-name")
item_list_2 = [veg.text for veg in veggies]

originalAmount = driver.find_element_by_css_selector(".discountAmt").text
# now in Cart page
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
# explicit way to hold the script
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
# implicit way to hold the script
print(driver.find_element_by_css_selector("span.promoInfo").text)

print(item_list_1)
print(item_list_2)
# validate whether products in page 1 are showing in page 2 check page
assert item_list_1 == item_list_2

discountAmount = driver.find_element_by_css_selector(".discountAmt").text
# verify if price decreases on discount
assert float(discountAmount) < float(originalAmount) # remember to convert str to float

# verify the summation of item amount
price_elements = driver.find_elements_by_css_selector("p.amount")
price_list = [float(price_element.text) for index, price_element in enumerate(price_elements) if index % 2 == 0]
'''
Another way to locate the correct table element is to find the correct path to table structure
"tbody tr td:nth-child(5) p.amount"
'''
total_price = float(driver.find_element_by_css_selector("span.totAmt").text)
print("Verify whether shopping list price: {} \n is equal to print total of {}" .format(price_list, total_price))
assert sum(price_list) == total_price

time.sleep(2)
driver.close()

'''
Q: When to use explicit wait vs. implicit wait?
A: If you think the load issue will only be in specific areas in the automation -- go to explicit wait
'''
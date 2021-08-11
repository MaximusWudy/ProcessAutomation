import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

# //div[@class='card h-100']/div/h4/a
# product = //div[@class='card h-100']
for product in products:
    product_name = product.find_element_by_xpath("div/h4/a").text # when start from middle, no need '//'
    if 'blackberry' in product_name.lower():
        product.find_element_by_xpath("div/button[@class='btn btn-info']").click()
        break

driver.find_element_by_css_selector("a.btn-primary").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

# auto-fill address
driver.find_element_by_id("country").send_keys("ind")
# explicit wait
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_css_selector("div[class='checkbox checkbox-primary']").click()
assert driver.find_element_by_css_selector("div[class='checkbox checkbox-primary'] input#checkbox2").is_selected()
driver.find_element_by_css_selector("[type='submit']").click()

successText = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in successText

# take screenshot
driver.get_screenshot_as_file("screen.png")

time.sleep(2)
driver.close()
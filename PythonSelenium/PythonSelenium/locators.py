from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='F:\\selenium\chromedriver.exe') # create a driver object
driver.get("https://rahulshettyacademy.com/angularpractice/")

'''
WebDriver Locators:
ID - findElementByID
Name
XPath: //tagname[@attr = value] -- tagname optional, Reg Ex: [contains(@attr, 'value')], [contains(text(), 'Password']
CSS (mostly suggested): tagname[attr = 'value'] -- tagname optional, Reg Ex: [attr *= 'value'], 
    ID Locator: tagname#username -- tagname optional
    Class locator: tagname.password -- tagname optional
ClassName: not recommended since it gets you multiple results
linkText
'''
# Enter name in the edit box
driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_css_selector("input[name='email']").send_keys("Rahul@gmail.com") # test it in your console: $("input[name='name']")
# selector will scan from left to right, up to down, use the 1st one it received
driver.find_element_by_id("exampleCheck1").click()

# handle static dropdown, select() class provides the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
dropdown.select_by_visible_text("Female") # select text from the screen
dropdown.select_by_index(0) # index starts from 0
# dropdown.select_by_value("sth") # for those <option value='sth'

driver.find_element_by_xpath("//input[@type='submit']").click() # test it in your console: $x("//input[@type='submit']")

# X path and CSS: independent of the developer declaration (compared with ID, Name...)

'''
Super useful plugin: ChroPath
it can auto generate xpath for you and you can also use it to check your xpath
'''

submit_result = driver.find_element_by_class_name("alert-success").text # print return text in the output

# use assert statement to validate success
assert 'success' in submit_result

time.sleep(3)
driver.close()
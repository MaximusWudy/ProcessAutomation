from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='F:\\selenium\chromedriver.exe')
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("rahul")
driver.find_element_by_css_selector(".password").send_keys("shetty")
time.sleep(1)
driver.find_element_by_css_selector(".password").clear() # clear the text field

# search by linked text: <a href='www.aa.com' text /a>
driver.find_element_by_link_text("Forgot Your Password?").click()

# //tagname[text()='xxx'] use xpath based on text
driver.find_element_by_css_selector("[value='Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
time.sleep(3)
driver.close()

'''
Parent Child Traverse Mechanism
XPath: //div[@id='usernamegroup']/label[@for='username']
    //form[@name='login']/div[1]/label -- select the first occurrence of <div /div>
CSS: div[id='usernamegroup'] label[for='username']
    form[name='login'] label:nth-child(2) -- select the 2nd occurrence
'''
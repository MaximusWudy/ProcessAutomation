import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path='F:\\selenium\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

validationText = "Rahul"
driver.find_element_by_css_selector("input[id='name'][name='enter-name']").send_keys(validationText)
driver.find_element_by_css_selector("input[id='alertbtn']").click()
alert = driver.switch_to.alert # create alert object by switch from driver to alert mode
print(alert.text) # extract text from the alert

assert validationText in alert.text
alert.accept() # select 'OK'

# want to click 'Cancel'
# alert.dismiss()


time.sleep(2)
driver.close()
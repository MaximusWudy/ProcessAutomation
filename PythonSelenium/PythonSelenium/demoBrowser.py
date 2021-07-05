from selenium import webdriver
# browser exposes an executable file
# through selenium test we need to invoke the executable file
# which will then invoke actual browser
driver = webdriver.Chrome(executable_path='F:\\selenium\chromedriver.exe') # create a driver object

driver.get("https://rahulshettyacademy.com/") # get method to hit url on browser

# get web title
print(driver.title)

# validate whether we are still in the expected url
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back() # browser back
driver.refresh() # browser refresh

# close the browser
driver.close()
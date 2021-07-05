from selenium import webdriver
driver = webdriver.Chrome(executable_path='F:\\selenium\chromedriver.exe')

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
# use tagname to locate element
driver.find_element_by_tag_name("h3")

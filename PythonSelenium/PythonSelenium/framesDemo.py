import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\selenium\chromedriver.exe')
driver.get("https://the-internet.herokuapp.com/iframe")
'''
Frames come on top of HTML so selenium will have knowledge on only html level
Frame, iFrame, FrameSet

Leverage switch_to method again
Args: pass either frame id, or frame name or index value
'''
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("Hello World.")
# come back to default HTML
driver.switch_to.default_content()

print(driver.find_element_by_tag_name("h3").text)

time.sleep(2)
driver.close()
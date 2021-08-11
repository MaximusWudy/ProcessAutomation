import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PySeleniumFramework.utilities.BaseClass import BaseClass
from PySeleniumFramework.pageObjects.HomePage import HomePage
from PySeleniumFramework.pageObjects.CheckoutPage import CheckoutPage

'''Notes:
* Parsing command line options: put in conftest.py
* Page object mechanism: for each page, we will have a designated class for it

* html report
py.test --html=report.html
'''
# @pytest.mark.usefixtures("setup") # use fixture for launching the browser, or get the knowledge into the parent class
class TestOne(BaseClass):

    def test_e2e(self, setup):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        # in order to access class object, use self.object
        homePage.shopItems().click() # same as "self.driver.find_element_by_css_selector("a[href*='shop']").click()"
        log.info("getting all the card titles")
        checkoutPage = CheckoutPage(self.driver)
        products = checkoutPage.getCardTitles()
        # //div[@class='card h-100']/div/h4/a
        # product = //div[@class='card h-100']
        i = -1
        for product in products:
            i += 1
            product_name = product.text  # when start from middle, no need '//'
            if 'blackberry' in product_name.lower():
                checkoutPage.getCardFooter()[i].click()
                break

        self.driver.find_element_by_css_selector("a.btn-primary").click()
        checkoutPage.checkOutItems().click()
        log.info("Entering country name as ind")
        # auto-fill address
        self.driver.find_element_by_id("country").send_keys("ind")

        self.verifyLinkPresence("India")

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_css_selector("div[class='checkbox checkbox-primary']").click()
        assert self.driver.find_element_by_css_selector(
            "div[class='checkbox checkbox-primary'] input#checkbox2").is_selected()
        self.driver.find_element_by_css_selector("[type='submit']").click()

        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText
        # assert "Success! But no Thank you!" in successText # make the test fail

        # take screenshot
        self.driver.get_screenshot_as_file("screen.png")

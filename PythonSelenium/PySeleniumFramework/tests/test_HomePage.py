from PySeleniumFramework.utilities.BaseClass import BaseClass
from PySeleniumFramework.pageObjects.HomePage import HomePage
import pytest

from PySeleniumFramework.TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData): # pass the fixture to the test_xx method

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData[0]) # only need 1 level since each element is a test run
        homepage.getEmail().send_keys(getData[1]) # can change to using dictionary for better readable
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData[2])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert "Success" in alertText
        print(alertText)

        # refresh browser for the next set of test params
        self.driver.refresh()

    # if not global usage, the fixture should not be in the conftest.py file
    # fixture will load all test data before the test execution start
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

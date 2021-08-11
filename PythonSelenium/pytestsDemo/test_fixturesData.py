import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editProfile(self, dataLoad): # return something from the fixture, should pass the fixture name
        logger = self.getLogger()
        logger.info(dataLoad[0])
        logger.info(dataLoad[2])
        print(dataLoad)


'''
use py.test --html=report.html -s to run all the test cases
* any logger information will be printed in your html output, which is GREAT
'''
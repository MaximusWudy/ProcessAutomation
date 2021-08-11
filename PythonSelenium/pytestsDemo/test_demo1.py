'''
SYNTAX REQUIREMETN
Any pytest file should start with 'test_' prefix, OR with '_test' suffix

pytest requires test method name, start with 'test_'

any code should be wrapped in method only

In command line (recommended):
py.test -v (for verbose) executed in the destination folder -s (print all the console logs)

Note: in pytest, the testing method/function names should be unique

!! Run specific test function in all files using regex
py.test -k CreditCard -v -s

!! Mark test cases with decorator and -m
@pytest.mark.smoke
then
py.test -m smoke -v -s

!! Skip a test
@pytest.mark.skip

!! just running but not reporting (if the method is required for other cases to run, but should hide in reporting)
@pytest.mark.xfail

!! Fixture: setup methods before test methods, as prerequisite or after testing; 'conftest.py' allows fixture to be
available for all test cases

!! parameterization: datadrive and parameterization can be done wiht return statements in tuple format

!! html report: pip install pytest-html
py.test --html=report.html
'''
import pytest

@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

def test_SecondGreetCreditCard():
    print("Good morning!")

def test_crossBrowser(crossBrowser): # we have 3 params, so the test will run 3 times
    print(crossBrowser)

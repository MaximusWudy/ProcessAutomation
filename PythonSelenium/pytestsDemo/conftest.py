'''
Use exactly the same file name "conftest.py"
then, if define the @pytest.fixture()
it will be available for all pytest test file 'test_xxx.py' with 'test_functionname' in the folder
searching order: local file >> conftest.py
'''
# define a fixture
import pytest

@pytest.fixture(scope="class") # if arg: scope="class", then setup is run before and after each class instance
def setup(): # like a prerequisite
    print("I will be executing first")
    yield # where the testing methods will be inserted
    print("I will execute last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]

@pytest.fixture(params=[["chrome", "Rahul"], "Firefix", "IE"]) # test multiple variants using params
def crossBrowser(request):
    return request.param

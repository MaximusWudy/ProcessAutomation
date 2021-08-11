import pytest

@pytest.mark.smoke
@pytest.mark.skip # predefined marks
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because condition do not match"

def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"

# define a fixture
@pytest.fixture()
def setup(): # like a prerequisite
    print("I will be executing first")
    yield # where the testing methods will be inserted
    print("I will execute last")

def test_fixtureDemo(setup): #then program runs this, with connection to the setup test
    print("I will execute steps in fixtureDemo method")
import pytest

@pytest.mark.usefixtures("setup") # apply fixture to all methods in the class (do not need to specify in each cases)
class TestExample:
    def test_fixtureDemo(self):
        print("fixture Demo 0")

    def test_fixtureDemo1(self):
        print("fixture Demo 1")

    def test_fixtureDemo2(self):
        print("fixture Demo 2")

    def test_fixtureDemo3(self):
        print("fixture Demo 3")
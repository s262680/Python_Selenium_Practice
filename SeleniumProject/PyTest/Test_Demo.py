import pytest

#excute before every test method
#@pytest.fixture()
#def setup():
    #print("Print once before every method")

#excute before and after every test method
@pytest.yield_fixture()
def setup():
    print("Print once before every method")
    yield
    print("Print once after every method")

def testMethod1(setup):
    print("This is a test method 1")

def testMethod2():
    print("This is a test method 2")


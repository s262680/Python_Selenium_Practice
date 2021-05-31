import pytest

#excute before and after every test method
@pytest.yield_fixture()
def setup():
    print("Opening URL to login")
    yield
    print("Closing Browser after login")

def test_loginByEmail(setup):
    print("This is login by email test")

def test_loginByFacebook(setup):
    print("This is login by facebook test")

import pytest

#excute before and after every test method
@pytest.yield_fixture()
def setup():
    print("Opening URL to signup")
    yield
    print("Closing Browser after signup")

def test_signupByEmail(setup):
    print("This is signup by email test")

def test_signupByFacebook(setup):
    print("This is signup by facebook test")

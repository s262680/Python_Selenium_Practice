import unittest
from SeleniumProject.UnitTestingSuites.Package1.TC_LoginTest import LoginTest
from SeleniumProject.UnitTestingSuites.Package1.TC_SignupTest import SignupTest

from SeleniumProject.UnitTestingSuites.Package2.TC_PaymentTest import PaymentTest
from SeleniumProject.UnitTestingSuites.Package2.TC_PaymentReturnsTest import PaymentReturnsTest

#Get all test from LoginTest, SignupTest, PaymentTest and PaymentReturnsTest
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#Creating test suites
sanityTestSuite=unittest.TestSuite([tc1,tc2]) # Sanity test suite
FunctionalTestSuite=unittest.TestSuite([tc3,tc4]) # Functional test suite
MasterTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4]) # Master test suite

#excute suite (verbosity=2 provide more info in the console)
unittest.TextTestRunner(verbosity=2).run(MasterTestSuite)



import unittest
from maintest.test.TestBed import TestBed
from maintest.pages.Login import Login
from pyunitreport import HTMLTestRunner

class TestMobile(TestBed):

  # def test_sample(self):
  #  print("*********TESTCASE STARTED*********")
  #  self.driver.find_element_by_id("joinNowButton").click()
  #  self.driver.find_element_by_id("googleSignUpButton").click()
  #  self.driver.find_element_by_xpath("//*[@text='qapremise18@gmail.com']").click()
  #  self.driver.find_element_by_class_name()
  #  self.driver.find_elements_by_class_name()


  def test_login(self):
      print(">>>>test LOGIN>>>>>")
      login = Login(self.driver)
      login.verifyUserLogin("NewGmailPublicUser","US")
      # self.driver.find_elements_by_id()


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='testreport'))


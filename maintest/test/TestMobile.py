import unittest
from maintest.TestBed import TestBed
class TestMobile(TestBed):

  def test_sample(self):
   print("*********TESTCASE STARTED*********")
   self.driver.find_element_by_id("joinNowButton").click()
   self.driver.find_element_by_id("googleSignUpButton").click()
   self.driver.find_element_by_xpath("//*[@text='qapremise18@gmail.com']").click()
if __name__ == '__main__':
    unittest.main()

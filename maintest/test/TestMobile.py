import unittest
from maintest.TestBed import TestBed
class TestMobile(TestBed):

  def test_sample(self):
   print("HIIIIIIIi")
   self.driver.find_element_by_id("joinNowButton").click()
   self.driver.find_element_by_id("googleSignUpButton").click()
   self.driver.find_element_by_id("googleSignUpButton").click()
if __name__ == '__main__':
    unittest.main()

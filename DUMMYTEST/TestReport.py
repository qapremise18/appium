import unittest
from pyunitreport import HTMLTestRunner

class TestReport(unittest.TestCase):

    def test_sampletest(self):
        print("PASSSSS")


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='testreport'))
    # unittest.main()

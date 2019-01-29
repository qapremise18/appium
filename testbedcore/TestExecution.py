import unittest
from maintest import MobileTest

if __name__ == "__main__":

    test = unittest.TestLoader().loadTestsFromTestCase(MobileTest)
    unittest.TextTestRunner(verbosity=2).run(test)
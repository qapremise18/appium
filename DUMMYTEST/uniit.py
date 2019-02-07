import unittest
from DUMMYTEST.classB import classB
class uniit:

 def java(self):
     # if __name__ == "__main__":
     test = unittest.TestLoader().loadTestsFromTestCase(classB)
     loader = unittest.TestLoader()
     suite = loader.loadTestsFromNames([classB])

    # loader = unittest.TestLoader()
    # start_dir = 'D:\\PythonWS\\Premise\\DUMMYTEST\\classB.py'
    # suite = loader.discover(start_dir)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)



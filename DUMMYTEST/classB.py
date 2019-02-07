from DUMMYTEST.classA import classA
import unittest
class classB(classA) :
    def test_1(self):
        print("bye22")
    def test_2(self):
        print("method2")

if __name__ == "__main__":
    unittest.main()



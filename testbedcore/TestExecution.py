import unittest
from maintest.TestMobile import TestMobile
from testbedcore.TestBedConfig import TestBedConfig

if __name__ == "__main__":
    testConfig = TestBedConfig()
    testConfig.readConfig("D:\\PythonWS\\Premise\\resources\\config.properties")

    # test = unittest.TestLoader().loadTestsFromTestCase(MobileTest)
    # loader = unittest.TestLoader()
    # suite = loader.loadTestsFromNames([MobileTest])

    # loader = unittest.TestLoader()
    # start_dir = 'D:\\PythonWS\\Premise\\maintest\\TestMobile.py'
    # suite = loader.discover(start_dir)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMobile)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # loader = unittest.TestLoader()
    # suite = unittest.TestSuite()
    # suite.addTests(loader.loadTestsFromModule(player))
    # suite.addTests(loader.loadTestsFromModule(scenario))
    # suite.addTests(loader.loadTestsFromModule(thing))
    # runner = unittest.TextTestRunner(verbosity=3)
    # result = runner.run(suite)

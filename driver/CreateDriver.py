from testbedcore import AppiumLauncher, TestBedConfig
from appium import webdriver
import sys
class CreateDriver:

 def createLocalDriver(self, capabilities, testBedConfig, testBedName) :
        driver = None
        self.capabilities = capabilities
        self.testBedConfig = testBedConfig
        print("*****Start createLocalDriver method*******")
        # serverUrl = "http://" + "127.0.0.1"+ ":" + testBedConfig.testBedName) +"/wd/hub")
        serverUrl = "http://127.0.0.1:4723/wd/hub"
        try :
            print("*****Start createLocalDriver method*******")
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.capabilities)
            driver.implicitly_wait(20)
            print("AppiumDriver successfully created:::createLocalDriver")
        except :
            print("Error while createLocalDriver:::"+sys.exc_info())
            print("Throwable while createLocalDriver:::")

 def getDriverTest(self):
     return self.driver

 def getDriver(capabilities, testBedConfig, testBedName):
      driver = None
      CreateDriver.createLocalDriver(capabilities, testBedConfig, testBedName)
      return driver;
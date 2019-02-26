from testbedcore import AppiumLauncher, TestBedConfig
from appium import webdriver
import sys
class CreateDriver:

 def createLocalDriver(self, capabilities, testBedConfig, testBedName) :
        self.driver = None
        self.capabilities = capabilities
        self.testBedConfig = testBedConfig
        print(">>>>>self.capabilities",self.capabilities)
        print(">>>>>self.testBedConfig", self.testBedConfig)
        print("*****Start createLocalDriver method*******")
        # serverUrl = "http://" + "127.0.0.1"+ ":" + testBedConfig.testBedName) +"/wd/hub")
        # serverUrl = "http://127.0.0.1:4723/wd/hub"
        try :
            print("*****Start createLocalDriver method*******")
            # self.driver = webdriver.Remote("http://127.0.0.1:4200/wd/hub", self.capabilities)
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.capabilities)
            self.driver.implicitly_wait(20)
            print("AppiumDriver successfully created:::createLocalDriver")
        except :
            print("Error while createLocalDriver:::",sys.exc_info())
            print("Throwable while createLocalDriver:::")
        return self.driver

 def getDriverTest(self):
     return self.driver

 def getDriver(self, capabilities, testBedConfig, testBedName):
      driver = None
      return self.createLocalDriver(capabilities, testBedConfig, testBedName)
      # return driver
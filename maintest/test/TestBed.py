from testbedcore.TestBedConfig import TestBedConfig
from testbedcore.AppiumLauncher import AppiumLauncher
from testbedcore.DeviceCapabilities import DeviceCapabilities
from driver.CreateDriver import CreateDriver
import sys, time, unittest

class TestBed(unittest.TestCase):

    # def __init__(self):
    #     self.testBedConfig = TestBedConfig()
    #     self.testBedConfig.readConfig("D:\\PythonWS\\Premise\\resources\\config.properties")
    #     # testBedConfig = TestBedConfig.test.getdriverinstance()
    #     self.driverInstance = self.testBedConfig.getdriverinstance()
    #     # self.testBedConfig = TestBedConfig()
    #     # self.testBedConfig.getdriverinstance()


    def setUp(self):
      try :
            self.testBedConfig = TestBedConfig()
            self.testBedConfig.readConfig("D:\\PythonWS\\Premise\\resources\\config.properties")
            self.driverInstance = self.testBedConfig.getdriverinstance()
            print("testBedConfig.getTestBedName>>>", self.testBedConfig.getTestBedName())
            print("testBedConfig.getTestBedName22>>>", self.testBedConfig.getPort())
            self.appLaunchObj = AppiumLauncher()
            self.appLaunchObj.closeAppiumSession(self.testBedConfig.getPort())
            print("getPort>>>" , self.testBedConfig.getTestBedName())
            print("TestBedName>>>", self.testBedConfig.getTestBedName())
            self.driverInit(self.testBedConfig.getTestBedName())
            # loginTest = Login(testBedConfig.getDriver())
            # taskTest = Tasks(testBedConfig.getDriver())
            # taskHistoryTest = TaskHistory(testBedConfig.getDriver())
            # paymentTest = Payment(testBedConfig.getDriver())
            # settingTest = Settings(testBedConfig.getDriver())
      except:
            print("Unable to load the property file::: " , sys.exc_info())

    def driverInit(self, testBedName) :
        # testBedConfig = TestBedConfig.getInstance()
        print("Initializing Android driver for testBedName:::" , testBedName)
        self.driver = None
        try :
            # app = AppiumLauncher()
            # app.launchAppiumSession(self.testBedConfig, testBedName)
            devcap = DeviceCapabilities()
            #cap =  devcap.setMobileDeviceCapabilities
            crd = CreateDriver()
            self.driver = crd.getDriver(devcap.setMobileDeviceCapabilities(self.testBedConfig, testBedName),self.testBedConfig,
            testBedName)
            print("Driver created is :::", self.driver)
            self.testBedConfig.setDriver(self.driver)
        except :
                print("Unable to initialize driver :::",  sys.exc_info())



    def launchApp(self):
        # testBedConfig = self.testBedConfig.getdriverinstance()
        self.testBedConfig = TestBedConfig()
        self.testBedConfig.readConfig("D:\\PythonWS\\Premise\\resources\\config.properties")
        self.driverInstance = self.testBedConfig.getdriverinstance()

        try :
            # AppiumLauncher.executeCommand("adb -s " + self.testBedConfig.getUdid()
            #         + " shell am start -n " + self.testBedConfig.config.getValue("APPIUM_CONFIG", "APPPACKAGE") + "/"
            #         + self.testBedConfig.config.getValue("APPIUM_CONFIG", "APPACTIVITY"))
            AppiumLauncher.executeCommand("adb -s " + self.testBedConfig.getUdid()
                                          + " shell am start -n " + self.testBedConfig.getappPackage()+ "/"
                                          + self.testBedConfig.getappActivity())
            time.sleep(5)
            print("Relaunched App")
        except :
            print("Unable to re launch App:::" , sys.exc_info())

    def closeAndRelaunchApp(self) :
        print("In closeAndRelaunchApp()::::")
        self.closeApp()
        self.relaunchApp()


    def closeApp(self) :
        testBedConfig = self.testBedConfig.getdriverinstance()
        AppiumLauncher.executeCommand("adb -s " + testBedConfig.getUdid()
                + " shell am force-stop " + testBedConfig.appPackage)
        print("Closing the app")


    def relaunchApp(self) :
        testBedConfig = self.testBedConfig.getdriverinstance()
        AppiumLauncher.executeCommand("adb -s " + testBedConfig.getUdid()+ " shell am start -n " +
                                      testBedConfig.appPackage + "/" + testBedConfig.appActivity)
        print("Re launching app after closing app")
        time.sleep(3000)
        print("App Relaunched")

    def clearAppDataAndLaunchApp2(self):
        self.clearAppData()
        self.launchApp()
        testBedConfig = self.testBedConfig.getdriverinstance()
        # testBedConfig.getDriver().resetApp()
        print("Relaunched App")

    def clearAppData(self):
        self.testBedConfig = TestBedConfig()
        self.testBedConfig.readConfig("D:\\PythonWS\\Premise\\resources\\config.properties")
        self.driverInstance = self.testBedConfig.getdriverinstance()

        # testBedConfig = self.testBedConfig.getdriverinstance()
        print("testBedConfig#########",self.testBedConfig)
        print("testBedConfig#########", self.testBedConfig==None)
        print("testBedConfig#########", self.driverInstance == None)
        print("testBedConfig#########", self.testBedConfig.getUdid())
        # AppiumLauncher.executeCommand("adb -s " + self.testBedConfig.getUdid()
        #                               + " shell pm clear " + self.testBedConfig.config.getValue("APPPACKAGE"))
        AppiumLauncher.executeCommand("adb -s " + self.testBedConfig.getUdid()
                                      + " shell pm clear " + self.testBedConfig.getappPackage())
        time.sleep(3)
        time.sleep(3)
        print("Cleared App data")
    def tearDown(self):
        # testBedConfig = TestBedConfig.getInstance()
        try :
            if (self.testBedConfig.getDriver() == None) :
                print("Unable to close appium as driver is null")
            else :
                self.testBedConfig.getDriver().quit()
        except :
            print("Exception encountered in driverCleanUp():::" + sys.exc_info())
        finally :
            if self.appLaunchObj.closeAppiumSession(self.testBedConfig.getPort()) == False:
                print("Appium session clean up not successfull")

# if __name__ == '__main__':
#     unittest.main()
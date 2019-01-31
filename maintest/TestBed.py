from testbedcore.TestBedConfig import TestBedConfig
from testbedcore.AppiumLauncher import AppiumLauncher
from testbedcore.DeviceCapabilities import DeviceCapabilities
from driver.CreateDriver import CreateDriver
import sys, time, unittest

class TestBed(unittest.TestCase):

    def setUp(self):
      try :
            self.testBedConfig = TestBedConfig()
            self.testBedConfig.readConfig("D:\\PythonWS\\Premise\\resources\\config.properties")
            # testBedConfig = TestBedConfig.test.getdriverinstance()
            self.driverInstance = self.testBedConfig.getdriverinstance()
            print("testBedConfig.getTestBedName>>>", self.testBedConfig.getTestBedName())
            print("testBedConfig.getTestBedName22>>>", self.testBedConfig.getPort())
            AppiumLauncher.closeAppiumSession(self.testBedConfig.getPort())
            print("getPort>>>" + self.testBedConfig.getTestBedName())
            print("TestBedName>>>"+ self.testBedConfig.getTestBedName())
            self.driverInit(self.testBedConfig.getTestBedName())
            # loginTest = Login(testBedConfig.getDriver())
            # taskTest = Tasks(testBedConfig.getDriver())
            # taskHistoryTest = TaskHistory(testBedConfig.getDriver())
            # paymentTest = Payment(testBedConfig.getDriver())
            # settingTest = Settings(testBedConfig.getDriver())
      except:
            print("Unable to load the property file::: " + sys.exc_info())

    def driverInit(self, testBedName) :
        # testBedConfig = TestBedConfig.getInstance()
        print("Initializing Android driver for testBedName:::" + testBedName)
        driver = None
        try :
            app = AppiumLauncher()
            app.launchAppiumSession(self.testBedConfig, testBedName)
            devcap = DeviceCapabilities()
            #cap =  devcap.setMobileDeviceCapabilities
            crd = CreateDriver()
            driver = crd.getDriver(devcap.setMobileDeviceCapabilities(self.testBedConfig, testBedName),self.testBedConfig,
            testBedName)
            print("Driver created is :::" + driver.toString())
            self.testBedConfig.setDriver(driver)
        except :
                print("Unable to initialize driver :::" + sys.exc_info())



    def launchApp(self):
        testBedConfig = TestBedConfig.getInstance()
        try :
            AppiumLauncher.executeCommand("adb -s " + testBedConfig.getUdid()
                    + " shell am start -n " + testBedConfig.config.getValue("APPIUM_CONFIG", "APPPACKAGE") + "/"
                    + testBedConfig.config.getValue("APPIUM_CONFIG", "APPACTIVITY"))
            time.sleep(5)
            print("Relaunched App")
        except :
            print("Unable to re launch App:::" + sys.exc_info())

    def closeAndRelaunchApp() :
        print("In closeAndRelaunchApp()::::")
        TestBed.closeApp()
        TestBed.relaunchApp()


    def closeApp() :
        testBedConfig = TestBedConfig.getInstance()
        AppiumLauncher.executeCommand("adb -s " + testBedConfig.getUdid()
                + " shell am force-stop " + testBedConfig.appPackage)
        print("Closing the app")


    def relaunchApp() :
        testBedConfig = TestBedConfig.getInstance()
        AppiumLauncher.executeCommand("adb -s " + testBedConfig.getUdid()+ " shell am start -n " + testBedConfig.appPackage + "/" + testBedConfig.appActivity)
        print("Re launching app after closing app")
        time.sleep(3000)
        print("App Relaunched")


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
            if AppiumLauncher.closeAppiumSession(self.testBedConfig.getPort) ==  True:
                print("Appium session clean up not successfull")

# if __name__ == '__main__':
#     unittest.main()
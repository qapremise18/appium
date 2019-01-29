from testbedcore import AppiumLauncher,TestBedConfig,DeviceCapabilities
from driver import CreateDriver
import sys,time
class TestBed :
    def prepareBeforeTest(configParameters) :
      try :
            testBedConfig = TestBedConfig.test.getdriverinstance()
            print("testBedConfig.getTestBedName>>>", testBedConfig.getTestBedName)
            AppiumLauncher.closeAppiumSession(testBedConfig.getPort())
            TestBed.driverInit(testBedConfig.getTestBedName())

            # loginTest = Login(testBedConfig.getDriver())
            # taskTest = Tasks(testBedConfig.getDriver())
            # taskHistoryTest = TaskHistory(testBedConfig.getDriver())
            # paymentTest = Payment(testBedConfig.getDriver())
            # settingTest = Settings(testBedConfig.getDriver())
      except:
            print("Unable to load the property file::: " + sys.exc_info()[0])

    def driverInit(testBedName) :
        testBedConfig = TestBedConfig.getInstance()
        print("Initializing Android driver for testBedName:::" + testBedName)
        driver = None
        try :
            AppiumLauncher.launchAppiumSession(testBedConfig, testBedName)
            devcap = DeviceCapabilities()
            #cap =  devcap.setMobileDeviceCapabilities
            crd = CreateDriver()
            driver = crd.getDriver(DeviceCapabilities.setMobileDeviceCapabilities(testBedConfig, testBedName), testBedConfig,
            testBedName)
            print("Driver created is :::" + driver.toString())
            testBedConfig.setDriver(driver)
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


    def driverCleanUp():
        testBedConfig = TestBedConfig.getInstance()
        try :
            if (testBedConfig.getDriver() == None) :
                print("Unable to close appium as driver is null")
            else :
                testBedConfig.getDriver().quit()
        except :
            print("Exception encountered in driverCleanUp():::" + sys.exc_info())
        finally :
            if AppiumLauncher.closeAppiumSession(testBedConfig.getPort) ==  True:
                print("Appium session clean up not successfull")
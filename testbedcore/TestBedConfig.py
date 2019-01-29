# from .dir import AppiumLauncher
# from com.premise.driver import CreateDriver
# from ..AppiumLauncher import AppiumLauncher

import configparser
import sys
class TestBedConfig():
 deviceType = None
 screenSize = None
 maxWaitSeconds = 20
 maxImplicitWaitSeconds = 3
 maxInvisibletWaitSeconds = 3

 appiumVersion = None
 nodeJSPath = None
 screenRecord = None
 screenRecordPath = None
 appPackage = None
 appActivity = None
 udid = None
 device = None
 osVersion = None
 hub = "localhost"
 port = "4444"
 locale = None
 clearAppData = None
 takeScreenshot = None
 dataSheetPath = None
 screenshotPath = None
 customizedReportPath = None
 listeners = None
 testCoverage = None
 className = None
 testBedName = None

 currentTestBedMap = {}
 currentPortMap = {}
 driverMap = {}
 instance = None
 cap = None
 appiumLauncher = None
 createDriver = None
 driver = None
 props = None
 configFile = None
 config = None

 def __init__(self):
  pass

 instance = None
 appiumJSPath = None

 @classmethod
 def getdriverinstance(cls):
     if cls.instance is None:
         cls.instance = TestBedConfig()
     return cls.instance

 def getappiumpath(cls):
     return cls.appiumJSPath

 def readConfig(self, configFilePath):
     try:
         self.config = configparser.RawConfigParser()
         self.config.read(configFilePath)
         print(self.config.sections())
         self.setVariable(self.config)
     except:
            print("Exception in readConfig:::" + sys.exc_info()[0])

 def setVariable(self,config):
         try :
                maxWaitSeconds = int(config.get("WAITS", "MAX_WAIT_TIME_SECONDS"))
                maxImplicitWaitSeconds = int(config.get("WAITS", "IMPLICIT_WAIT_TIME_SECONDS"))
                maxInvisibletWaitSeconds = int(config.get("WAITS", "MAX_INVISIBLE_WAIT_TIME_SECONDS"))

                port = config.get("APPIUM_CONFIG", "PORT")
                nodeJSPath = config.get("APPIUM_CONFIG", "NODEJSPATH")
                appiumJSPath = config.get("APPIUM_CONFIG", "APPIUMJSPATH")
                appActivity = config.get("APPIUM_CONFIG", "APPACTIVITY")
                appPackage = config.get("APPIUM_CONFIG", "APPPACKAGE")
                locale = config.get("OTHER", "LOCALE")
                clearAppData = config.get("OTHER", "CLEARAPPDATA")
                screenRecord = config.get("SCREENRECORD", "SCREENRECORD")
                dataSheetPath = config.get("PATH", "DATASHEETPATH")
                screenshotPath = config.get("PATH", "SCREENSHOTPATH")
                testBedName = config.get("TESTNG", "TESTBED")
                udid = config.get("DeviceFarm", testBedName)
                listeners = config.get("TESTNG", "LISTENER")
                className = config.get("TESTNG", "CLASSNAME")
                testCoverage = config.get("TESTNG", "TESTCOVERAGE")
         except:
             print("Exception in setVariable:::", sys.exc_info())

 def getAppiumJSPath(self):
         return TestBedConfig.appiumJSPath


 def setDriver(self, dr):
     self.driver = dr

 def getDriver(self):
     return self.driver
 def getPort(self):
     return self.config.get("APPIUM_CONFIG", "TESTBED")

 def getDevice(self):
     return TestBedConfig.device

 def getDeviceType(self):
     return TestBedConfig.deviceType

 def getUdid(self):
     return TestBedConfig.udid

 def isDeviceTypeAndroid(self):
    str = TestBedConfig.getDeviceType(self)
    if str == "Android":
        return True
    else:
        return False

 def getNodePath(self):
  return TestBedConfig.nodeJSPath

 def getLocale(self):
    return TestBedConfig.locale

 def getClearAppData(self):
    return TestBedConfig.clearAppData

 def getDataSheetPath(self):
    return TestBedConfig.dataSheetPath

 def getScreenshotPath(self):
    return TestBedConfig.screenshotPath


 def getTestBedName(self):
    return TestBedConfig.testBedName


 def getTestCoverage(self):
    return TestBedConfig.testCoverage

 def getClassName(self):
    return TestBedConfig.className


test = TestBedConfig()
test.readConfig("D:\\PythonWS\\Premise\\resources\\config.properties")

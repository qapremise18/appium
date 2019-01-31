# from .dir import AppiumLauncher
# from com.premise.driver import CreateDriver
# from ..AppiumLauncher import AppiumLauncher

import configparser
import sys
class TestBedConfig:
 # deviceType = None
 # screenSize = None
 # maxWaitSeconds = 20
 # maxImplicitWaitSeconds = 3
 # maxInvisibletWaitSeconds = 3
 #
 # appiumVersion = None
 # nodeJSPath = None
 # screenRecord = None
 # screenRecordPath = None
 # appPackage = None
 # appActivity = None
 # udid = None
 # device = None
 # osVersion = None
 # hub = "localhost"
 # port = "4444"
 # locale = None
 # clearAppData = None
 # takeScreenshot = None
 # dataSheetPath = None
 # screenshotPath = None
 # customizedReportPath = None
 # listeners = None
 # testCoverage = None
 # className = None
 # testBedName = None
 #
 # currentTestBedMap = {}
 # currentPortMap = {}
 # driverMap = {}
 # instance = None
 # cap = None
 # appiumLauncher = None
 # createDriver = None
 # driver = None
 # props = None
 # configFile = None
 # config = None

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
                self.maxWaitSeconds = int(config.get("WAITS", "MAX_WAIT_TIME_SECONDS"))
                self.maxImplicitWaitSeconds = int(config.get("WAITS", "IMPLICIT_WAIT_TIME_SECONDS"))
                self.maxInvisibletWaitSeconds = int(config.get("WAITS", "MAX_INVISIBLE_WAIT_TIME_SECONDS"))

                self.port = config.get("APPIUM_CONFIG", "PORT")
                self.nodeJSPath = config.get("APPIUM_CONFIG", "NODEJSPATH")
                self.appiumJSPath = config.get("APPIUM_CONFIG", "APPIUMJSPATH")
                self.appActivity = config.get("APPIUM_CONFIG", "APPACTIVITY")
                self.appPackage = config.get("APPIUM_CONFIG", "APPPACKAGE")
                self.locale = config.get("OTHER", "LOCALE")
                self.clearAppData = config.get("OTHER", "CLEARAPPDATA")
                self.screenRecord = config.get("SCREENRECORD", "SCREENRECORD")
                self.dataSheetPath = config.get("PATH", "DATASHEETPATH")
                self.screenshotPath = config.get("PATH", "SCREENSHOTPATH")
                self.testBedName = config.get("TESTNG", "TESTBED")
                self.udid = config.get("DeviceFarm", self.testBedName)
                self.listeners = config.get("TESTNG", "LISTENER")
                self.className = config.get("TESTNG", "CLASSNAME")
                self.testCoverage = config.get("TESTNG", "TESTCOVERAGE")
                print("Succees in reading config file")
         except:
             print("Exception in setVariable:::", sys.exc_info())

 def getAppiumJSPath(self):
         return self.appiumJSPath


 def setDriver(self, dr):
     self.driver = dr

 def getDriver(self):
     return self.driver

 def getPort(self):
     return self.port

 def getDevice(self):
     return self.device

 def getDeviceType(self):
     return self.deviceType

 def getUdid(self):
     return self.udid

 def isDeviceTypeAndroid(self):
    str = TestBedConfig.getDeviceType(self)
    if str == "Android":
        return True
    else:
        return False

 def getNodePath(self):
  return self.nodeJSPath

 def getLocale(self):
    return self.locale

 def getClearAppData(self):
    return self.clearAppData

 def getDataSheetPath(self):
    return self.dataSheetPath

 def getScreenshotPath(self):
    return self.screenshotPath


 def getTestBedName(self):
    return self.testBedName


 def getTestCoverage(self):
    return self.testCoverage

 def getClassName(self):
    return self.className


# test = TestBedConfig()
# test.readConfig("D:\\PythonWS\\Premise\\resources\\config.properties")

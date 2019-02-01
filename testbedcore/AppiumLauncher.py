import os,sys ,subprocess

# from maintest.TestBed import TestBed
class AppiumLauncher:

 def launchAppiumSession(self, testBedConfig, testBedName):
     # apptestBedConfig = self.testBedConfig
     # apptestBedName   = self.testBedName
     print("XXXXXXxx"+testBedName)
     # print("XXXXXXxx" + apptestBedName)
     print("2222" + testBedConfig.getNodePath())
     print("2222" + testBedConfig.getAppiumJSPath())
     print("2222" + testBedConfig.getPort())
     print("2222" + testBedConfig.getUdid())
     try:
         command = testBedConfig.getNodePath() +" "+testBedConfig.getAppiumJSPath() +" --address 127.0.0.1 --port "+\
                   testBedConfig.getPort() +" -U " +  testBedConfig.getUdid() + " --no-reset"
         print("CMD appium \n",command)
         AppiumLauncher.executeCommand(command)
     except:
         print("launchAppiumSession exception>>>"+ sys.exc_info())



 # def executeCommand(command):
 #     try:
 #        os.system(command)
 #     except:
 #        print("executeCommand exception>>>" + sys.exc_info())

 def executeCommand(command):
     try:
         returned_value = subprocess.call(command, shell=True)
         print('returned value:', returned_value)
     except:
        print("executeCommand exception>>>" + sys.exc_info())

 def closeAppiumSession(self, portNumber):
  try:
     print("Executing closeAppiumSession commmand on OS::: for port number:::" + portNumber)
     AppiumLauncher.executeCommand("taskkill /f /im node.exe")
     AppiumLauncher.executeCommand("taskkill /f /im adb.exe")
     return True
  except:
     print("Exception occured on closeAppiumSession method :::" + sys.exc_info())
     return False

# cc ="taskkill /f /im node.exe"
# AppiumLauncher.executeCommand(cc)
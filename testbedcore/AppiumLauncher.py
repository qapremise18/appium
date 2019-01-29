import os,sys
class AppiumLauncher:

 def launchAppiumSession(testBedConfig, testBedName):
     command = testBedConfig.getNodePath() +" "+testBedConfig.getAppiumJSPath() +"-a 127.0.0.1 -p "+testBedConfig.getPort() +" -U " + testBedConfig.getUdid() + " --no-reset"
     AppiumLauncher.executeCommand(command)

 def executeCommand(command):
     os.system(command)

 def closeAppiumSession(portNumber):
  try:
     print("Executing closeAppiumSession commmand on OS::: for port number:::" + portNumber)
     AppiumLauncher.executeCommand("taskkill /f /im node.exe")
     AppiumLauncher.executeCommand("taskkill /f /im adb.exe")
  except:
     print("Exception occured on closeAppiumSession method :::" + sys.exc_info())
     return False

# cc ="taskkill /f /im node.exe"
# AppiumLauncher.executeCommand(cc)
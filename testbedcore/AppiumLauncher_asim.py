import os, sys, subprocess, signal
from subprocess import Popen, PIPE, STDOUT

# from maintest.TestBed import TestBed
class AppiumLauncher:

 def launchAppiumSession(self, testBedConfig, testBedName):
     # apptestBedConfig = self.testBedConfig
     # apptestBedName   = self.testBedName

     print("******************** TEST BED NAME  ************ : " + testBedName)
     print("******************** Node_Path ***************** : " + testBedConfig.getNodePath())
     print("******************** AppiumJS_Path ************* : " + testBedConfig.getAppiumJSPath())
     print("******************** PORT NUMBER *************** : " + testBedConfig.getPort())
     print("******************** UDID  ********************* : " + testBedConfig.getUdid())
     #os.system("taskkill /F /IM node.exe")
     try:
         command1 = "taskkill " + "/" + "f " + "/" + "im " + "node.exe"
         command = testBedConfig.getNodePath() +" "+testBedConfig.getAppiumJSPath() +" --address 127.0.0.1 --port "+\
                   testBedConfig.getPort() +" -U " +  testBedConfig.getUdid() + " --no-reset" #+ " "+command1
         #+ command1

         command2 = "taskkill " + "/" + "f " + "/" + "im " + "adb.exe"
         print("CMD appium \n", command)
         print("CMD appium \n", command1)
         print("CMD appium \n", command2)

         # p1 = Popen(['open', '-a', 'Terminal', '-n'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
         # p2 = Popen(['open', '-a', 'Terminal', '-n'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
         #
         # p1.communicate('appium')
         # p2.communicate('appium -a 0.0.0.0 -p 4724')
         # p1.kill()
         # p2.killall()
         #AppiumLauncher.executeTaskKillCommand()

         AppiumLauncher.executeCommand(command, command1, command2)


         #

     except:
         print("launchAppiumSession exception>>>"+ sys.exc_info())



 # def executeCommand(command):
 #     try:
 #        os.system(command)
 #     except:
 #        print("executeCommand exception>>>" + sys.exc_info())

 def executeCommand(command,command1,command2):
     try:

         #subprocess.Popen(["mupdf", "/home/dan/Desktop/Sieve-JFP.pdf"])
         #subprocess.call(command, shell=True)

         si = subprocess.STARTUPINFO()
         si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
         subprocess.call(["taskkill", "/IM", "node.exe", "/T", "/F"], startupinfo=si)
         subprocess.Popen(command, )
         sys.exit(0)
         # os.system(command)
         # os._exit(0)
         # os.system("start /B start cmd.exe @cmd /k taskkill /F /IM node.exe")
         # si = subprocess.STARTUPINFO()
         # si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
         # subprocess.call(["taskkill", "/IM", "node.exe", "/T", "/F"], startupinfo=si)

         # pro = subprocess.Popen(command, stdout=subprocess.PIPE,
         #                        shell=True, preexec_fn=os.setsid)
         #
         # os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
         # os.system("start /B start cmd.exe @cmd /k taskkill /F /IM node.exe")
         # os.system(" cmd.exe")
         # os.system(command)
         #os.system("start /B start cmd.exe @cmd /k appium -a 127.0.0.1 -p 4728")





         #os.system(command)
         #sys.exit(0)

         #os.popen().close()
         #os.system("C:\\Users\\asingh\\AppData\\Local\\Programs\\appium-desktop\\resources\\app\\node_modules\\appium\\build\\lib\\main.js")
         #os.system("start /B start cmd.exe @cmd /k taskkill /F /IM node.exe")
         #node_exe = int(subprocess.check_output(['pgrep', '-f', 'node.exe']).strip())
         #pid = node_exe
         #os.kill(pid, signal.SIGTERM)
         #os.system(command1)
         #os.system(command2)


         #os.System("appium")
         #os.system("start /B start cmd.exe @cmd /k appium -a 127.0.0.1 -p 4728")
         #subprocess.call(command, shell=True)


         #subprocess.Popen.terminate()
         #returned_value = os.system(command)
         #subprocess.Popen.terminate()
         #os.close()
         #print('******** returned value: ******************* ', returned_value)
         #AppiumLauncher.executeTaskKillCommand()
         return True

     except:
        #print("executeCommand exception>>>" + sys.exc_info())
        return False

 def executeTaskKillCommand(self):
     try:
        p = subprocess.Popen("tasklist", stdout=subprocess.PIPE)
        RunningProcessLIst = p.stdout.readlines()
        command1 = "taskkill " + "/" + "f " + "/" + "im "+"node.exe"
        command2 = "taskkill " + "/" + "f " + "/" + "im "+"adb.exe"
        for runningPro in RunningProcessLIst:
            if "node.exe" in str(runningPro):
                print("*********  Kill all running instances of node.exe : ************ ", RunningProcessLIst)
                #subprocess.call(command1)
                si = subprocess.STARTUPINFO()
                si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                # subprocess.call(["taskkill", "/IM", "node.exe", "/T", "/F"], startupinfo=si)
                subprocess.Popen(command1, )
                #sys.exit(0)
                sys.exit(0)
            elif "adb.exe" in str(runningPro):
                    print("*********  Kill all running instances of adb.exe : ************ ", RunningProcessLIst)
                    #subprocess.call(command2)
                    si = subprocess.STARTUPINFO()
                    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    # subprocess.call(["taskkill", "/IM", "node.exe", "/T", "/F"], startupinfo=si)
                    subprocess.Popen(command1, )
                    sys.exit(0)
             # os.system("taskkill /F /IM adb.exe")
            #process = subprocess.Popen(
               # "C:\\Users\\asingh\\AppData\\Local\\Android\\Sdk\\platform-toolsadb.exe adb get-state")
           # process = subprocess.Popen(
               # "C:\\Progra~1\\nodejs\\node.exe")


     except:
        # print("Exception occured on closeAppiumSession method :::" + sys.exc_info())
          return False

 def closeAppiumSession(self, portNumber):
  try:
     print("Executing closeAppiumSession commmand on OS::: for port number:::" + portNumber)
     command1 = "taskkill" + "/"+"f"+" "+"/"+"im"+" "+"node.exe"
     command2 = "taskkill" + "/"+"f"+" "+"/"+"im"+" "+"adb.exe"
     AppiumLauncher.executeTaskKillCommand()
     #AppiumLauncher.executeCommand(command2)
     return True
  except:
     #print("Exception occured on closeAppiumSession method :::" + sys.exc_info())
     return False

# cc ="taskkill /f /im node.exe"
# AppiumLauncher.executeCommand(cc)
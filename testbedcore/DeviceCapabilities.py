class DeviceCapabilities():

 def setMobileDeviceCapabilities(self, testBedConfig, testBedName):
    desired_caps = {}
    if testBedConfig.getDeviceType() == "Android":
            print("Setting Desiered capabilities as below")
            desired_caps["deviceName"] = testBedName
            desired_caps["platformName"] = "Android"
            desired_caps["appPackage"] = testBedConfig.appPackage
            desired_caps["appActivity"] = testBedConfig.appActivity
            desired_caps["udid"] = testBedConfig.getTestBedMap().get(testBedName)
            desired_caps["platformVersion"] = testBedConfig.osVersion
            desired_caps["autoAcceptAlerts"] = True
            desired_caps["screenshotWaitTimeout"] = 60
            # if(DeviceInfo.isAndroidOreo())
			#     desired_caps["automationName", "uiautomator2")
    else:
        print("EORRRRRRRRR In Else pass")
    print("Capabilities for >>", testBedName, desired_caps)
    return desired_caps

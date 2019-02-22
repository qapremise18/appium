from util.ExcelReader import ExcelReader
from elementactions.Element import Element
from maintest.test.TestBed import TestBed
import time
from delayed_assert import expect, assert_expectations
from apicore.UserService import UserService

class Login(Element):
    def __init__(self,driver):
        Element.__init__(self,driver)
        excel = ExcelReader()
        self.localeData = excel.getDataInHashMap("login", "LocaleData")
        self.testData = excel.getDataInHashMap("login", "LoginTestData")
        self.locators = excel.getDataInHashMap("login", "Locators")
        self.loginEmailData = excel.getDataInHashMap("login", "LoginEmailData")
        # self.localeData = {}
        # self.testData = {}
        # self.locators = {}
        # self.loginEmailData = {}
        self.flag = False
        self.testBed = TestBed()
        self.loginType = ""
        self.emailId = ""

    def clearAppDataAndLaunchApp(self):
        self.testBed.clearAppDataAndLaunchApp2()

    def isUserOnboardingWelcomeScreen(self):
        time.sleep(3)
        return not self.isElementByLocatorNotDisplayed(self.locators["LoginButton"])

    def verifyCarousel(self):
        print("****verifyCarousel"*10)
        carouselList = None
        carouselList = self.getListOfElementsByLocator(self.locators["CarouselButton"])
        for i in range(0,4):
            expect(self.isElementSelected(carouselList[i]) == True,
                                        "Carousel bubble  not selected for carousel bubble number :::" +(i + 1).__str__())
            carouselBodyMessage = ""
            if (i == 0):
                continue
            else:
                expect(self.getElementText(self.locators["CarouselTitleText"])== self.localeData["CarouselTitleText"+(i + 1).__str__()],
                                          "CarouselTitleText not matched for carousel bubble number :::" +(i + 1).__str__())
                carouselBodyMessage = self.getElementText(self.locators["CarouselBodyText"])

            expect(carouselBodyMessage == self.localeData["CarouselBodyText"+(i + 1).__str__()],
                                      "CarouselText not matched for carousel bubble number :::" +(i + 1).__str__())
            expect(self.isElementByLocatorNotDisplayed(self.locators["JoinNowButton"]) == False,
                                     "'SIGN UP' Button not displayed for carousel bubble number :::" +(i + 1).__str__())
            expect(self.isElementByLocatorNotDisplayed(self.locators["LoginButton"]) == False,
                                     "'LOG IN' Button not displayed for carousel bubble number :::" +(i + 1).__str__())

            self.screenSwipeRight(0.90, 0.3, 0.1, 0.3)


    def navigateToSignInScreen(self):
        if "Existing" in self.loginType or "Existing":
            flag = self.click(self.locators["LoginButton"])
            expect(flag == True,
                   "Failed to click on 'LOG IN' button for login user type ::: ".join(self.loginType))
            self.verifyLoginWelcomeBackScreen()
        else:
            print("Else in navigateToSignInScreen")

    def verifyLoginWelcomeBackScreen(self):
        expect(self.isElementByLocatorNotDisplayed(self.locators["SignUpImage"]) == False,
               "SignUp Image not seen on Welcome back login screen")
        expect(self.getElementText(self.locators["SignUpTitle"]) == self.localeData["SignUpTitleWelcomeBack"],
               "Welcome back login title mismatched")
        expect(self.getElementText(self.locators["SignUpBodyText"]) == self.localeData["SignUpBodyText"],
               "Welcome back login subtitle mismatched")
        expect(self.isElementByLocatorNotDisplayed(self.locators["SignupGoogleButton"]) == False,
               "GoogleSignUpButton not seen on Sign up screen")
        expect(self.isElementByLocatorNotDisplayed(self.locators.get("LoginFacebookButton")) == False,
               "LoginFacebookButton not seen on Sign up screen")
        expect(self.isElementByLocatorNotDisplayed(self.locators["EnterPartnerCodeLink"]) == True,
               "'Enter partner code' link  button is seen on welcome back Sign up screen (i.e when users log out)")

        self.verifyLocalizationData("GoogleSignUpButton", "GoogleLoginButton", "GoogleLoginButton text not matched")
        self.verifyLocalizationData("LoginFacebookButton", "FacebookLoginButton",
                                    "FacebookLoginButton text not matched")
        self.verifyLocalizationData("ToggleUserLoginText", "ToggleUserSignUpText",
                                    "ToggleUserSignUpText text not matched")
        self.verifyLocalizationData("ToggleUserLoginButton", "SignUpLink", "SignUpLink text not matched")

    def verifyLocalizationData(self, element, locale, message):

        try:
            data = self.localeData[locale]
            commonEle = self.locators[element]
            if data == None:
                expect(False == True, "Locale data not added in localesheet for :::".join(locale))
                return
            elif commonEle == None:
                expect(False == True, "Locators data not added for :::".join(element))
                return
            flag = True
        except:
            expect(False == True, "Locale data not added in localesheet for :::" + locale)
            expect(False == True, "Locators data not added for :::" + element)
        return

    def termsConditionFlow(self):
        time.sleep(3)
        self.verifyLocalizationData("TermsAgreeButton", "TermsAgreeButton", "TermsAgreeButton text not matched.")
        self.verifyLocalizationData("TermsOfServiceButton", "TermsOfServiceButton",
                                    "TermsOfServiceButton text not matched.")
        self.verifyLocalizationData("PrivacyPolicyButton", "PrivacyPolicyButton",
                                    "PrivacyPolicyButton text not matched.")
        expect(self.getElementText(self.locators["TermsConditionHeader"]) == self.localeData["TermsConditionHeader"],
               "Terms and Condition Header text mismatched for login user type :::".join(self.loginType))
        expect(self.getElementText(self.locators["TermsConditionText"]) == self.localeData["TermsConditionText"],
               "Terms and Condition content sub text mismatched for login user type :::".join(
                   self.loginType))
        expect(self.isElementByLocatorNotDisplayed(self.locators["TermsCloseButton"]) == False,
               "TermsCloseButton not seen on T&C pop up")
        print("Click on 'Terms of Service' link on  Terms and conditions window")

        expect(self.isElementByLocatorNotDisplayed(self.locators["TermsOfServiceButton"]) == False,
               "Terms of Service link  NOT rendered for login user type :::" + self.loginType)
        self.clickOnTermsOfServiceLink()

        expect(self.isElementByLocatorNotDisplayed(self.locators["PrivacyPolicyButton"]) == False,
               "Privacy Policy link  NOT rendered for login user type :::" + self.loginType)
        print("Click on 'Privacy policy' link on  Terms and conditions window")
        # self.clickOnPrivacyPolicyLink()

    def clickOnTermsOfServiceLink(self):
        termsOfServiceWindow = expect(self.click(self.locators["TermsOfServiceButton"])== True,
                                                 "Failed to click on Terms of Service link during"
                                                 " new account creation for login user type :::"+self.loginType)
        if termsOfServiceWindow == True:
            expect(self.isElementByLocatorNotPresent(self.locators["TermsOfServiceToolBar"]) == False,
                   "TermsOfServiceToolBar not seen under AboutTermsOfService")
            time.sleep(5)
            expect(self.isElementByLocatorNotDisplayed(
                self.constructXpathUsingText(self.localeData["TermsOfServiceText"])) == False or
                   self.isElementByLocatorNotDisplayed(
                       self.constructXpathUsingContentDesc(self.localeData["TermsOfServiceText"])) == False,
                   "TermsOfServiceContent is empty under AboutTermsOfService")
            self.driver.back()
            time.sleep(2)
            return True

    def checkForNewUser(self, emailID) :
        us = UserService()
        return us.softDeleteUser(emailID)

    def isGoogleAccountPickerDisplayed(self):
        if self.isElementByLocatorNotDisplayed(self.locators["AccountPickerHeader"]) == False:
            self.verifyLocalizationData("GooglePickUpTitle", "GooglePickUpTitle", "GooglePickUpTitle text not matched")
            self.verifyLocalizationData("GooglePickUpSubTitle", "GooglePickUpSubTitle",
                                   "GooglePickUpSubTitle text not matched")
            self.verifyLocalizationData("GooglePickUpConsentText", "GooglePickUpConsentText",
                                   "GooglePickUpConsentText not matched")
            return True
        else:
            return False

    def isAccountNameExistAndisClicked(self):
        isAccountInList = False
        self.emailID = self.loginEmailData[self.loginType]
        print("Expected emailID" , self.emailId)
        try:
            accountNameList = []
            accountNameList = self.getListOfElementsByLocator(self.locators["AccountListName"])
            for ele in  accountNameList :
                    print("USER List ID" , ele.text)
                    if ele.text.lower() in self.emailId.lower():
                        ele.click()
                        isAccountInList = True
                        break
        except :
            isAccountInList = False
            print("Unable to add user")
        print("Is user account ::: " , self.emailId, " for account type:::" ,self.loginType
         + "::: found in google account picker :::> " ,isAccountInList)
        return isAccountInList

    def clickLoginGoogleButton(self):
        print("Clicking on 'SIGN WITH GOOGLE' button")
        return self.click(self.locators["SignupGoogleButton"])

    def loginNewGmailUser( self, loginType ):

        flag = self.clickLoginGoogleButton()
        if (flag):
            for i in range(0,5):
                accDisplayed = self.isGoogleAccountPickerDisplayed()
                if (accDisplayed):
                    if (self.isAccountNameExistAndisClicked() == False):
                     break
                else:
                    self.driver.back()
                    self.clickLoginGoogleButton()
                    flag = False
        else:
            return expect(flag == True,"Failed to click on 'Login with Google' button for login user type ::: "+ loginType)
        return flag

    def loginNewUser(self, loginType,newLogin) :
        print("emailId:-->" + self.emailId)
        self.checkForNewUser(self.emailId)
        if "NewGmail" in loginType :
            return self.loginNewGmailUser(loginType)


    def changeUserGeoLocation(self, emailID, country):
        ex = ExcelReader()
        partialUpdateUser = ex.getDataInHashMap("locale", "partialUpdateUser")
        partialUpdateUserPayLoad = partialUpdateUser[country]
        print("partialUpdateUserPayLoad from excel :::".join(partialUpdateUserPayLoad))
        us = UserService()
        return us.partialUpdateUserMethod(emailID, partialUpdateUserPayLoad)


    def handleCameraPermissionAllowPopUp(self):
        self.click(self.locators["ClickForPermission"])
        self.click(self.locators["PermissionAllowButton"])

    def completeWeatherTask(self):
        self.click(self.locators["WeatherStartTaskButton"])
        self.click(self.locators["WeatherLikeToday"])
        if self.isElementByLocatorNotDisplayed(self.locators["TakePhotoButton"]) == False :
            self.click(self.locators["TakePhotoButton"])
        else:
            self.click(self.locators["TakePicButton"])

        self.handleCameraPermissionAllowPopUp()

        self.click(self.locators["CapturePhotoButton"])
        self.click(self.locators["UsePhotoButton"])
        self.click(self.locators["TakePhotoButtonNext"])
        self.click(self.locators["ConfirmButton"])
        self.click(self.locators["WeatherTypcalAnswer"])
        recordLocation = ""
        if self.isElementByLocatorNotDisplayed(self.locators["RecordLocation"]):
            recordLocation = "RecordLocation"
        else:
            recordLocation = "RecordLocationOld"
        print("recordLocation:" , recordLocation)

        self.click(self.locators[recordLocation])
        self.click(self.locators["SubmitLocation"])
        self.click(self.locators["YesButton"])
        self.click(self.locators["ConfirmTaskSubmit"])
        self.click(self.locators["DoMoreTasksButton"])
        return True

    def isUserOnTaskScreen(self):
        time.sleep(3)
        return self.isElementByLocatorNotDisplayed(self.locators["TaskScreenButton"])

    def completeOnBoardingFlow(self):
        if self.isElementByLocatorNotDisplayed(self.locators["FindMyLocationButton"])== False:
            flag =  self.click(self.locators["FindMyLocationButton"])== True
            flag = expect(flag,"Unable to click on Find My Location Button")
            if (flag == False):
                return False
            self.handleLocationPermissionAllowPopUp()
            self.handlePhonePermissionAllowPopUp()

            # self.isElementInvisible(self.locators["AndroidProgressBar"])
            flag = self.click(self.locators["StartNowButton"]) == True
            expect(flag,"Unable to click on Start Now Button")
            if (flag == False):
                return False
        flag = self.completeWeatherTask()
        if flag == False:
            return False
        flag = self.isUserOnTaskScreen()
        return expect(flag == True, "My Task screen tab button not selected.")

    def handleLocationPermissionAllowPopUp(self):
        self.click(self.locators["PermissionAllowButton"])

    def handlePhonePermissionAllowPopUp(self):
        self.click(self.locators["PermissionAllowButton"])

    def verifyUserLogin(self, loginType, country):
        self.emailId = self.loginEmailData[loginType]
        self.loginType =loginType
        self.flag = True

        print("loginType::::::" + loginType)
        print("EMAIL ID:::::::::" + self.emailId)
        isLoginSuccess = False
        if self.loginEmailData is None or self.localeData is None :
             assert (False, "Login test failed as Login test data is null")
             return False
        self.clearAppDataAndLaunchApp()
        if self.flag == True and "New" in loginType and "Private" not in loginType :
            expect (self.isUserOnboardingWelcomeScreen() == True, "User is not on onboarding Welcome screen")
            print("User is on onboarding Welcome screen")
            carouselCount = self.verifyCarousel()

        print("Clicking on Sign IN")
        flag = expect(self.navigateToSignInScreen() == True, "Unable to click on Navigate to sign in screen")
        if (self.flag is False):
            return False
        print("Started Login validation for -->" + loginType)
        list = ["NewGmailPublicUser","NewFBPublicUser","NewGmailPrivateUserCALISU","NewGmailSuperPrivateUserDREAMS",
                "NewGmailPrivateUserIOSPRIVATE","NewFBSuperPrivateUserDREAMS","NewFBPrivateUserCALISU",
                "NewGmailPrivateUserEMPTYSTATE","","","",""]
        if(loginType in list):
            isLoginSuccess = expect(self.loginNewUser(loginType, True), "Unable to Login New User")
            if isLoginSuccess is False :
                 return False
            termsConditionCount = self.termsConditionFlow()
            isLoginSuccess = self.completeOnBoardingFlow()
            expect( isLoginSuccess == True, "Error in completing Onboarding flow")
            if isLoginSuccess is False:
                return False
            if "EMPTYSTATE" not in loginType:
                expect(self.changeUserGeoLocation(self.emailId, country) == True,
                              "Partial update user failed for loginType:::" + self.emailId + " and user >>>"
                              + self.emailId)
            self.testBed.launchApp()
            return isLoginSuccess












from util.ExcelReader import ExcelReader
from elementactions.Element import Element
from maintest.test.TestBed import TestBed
import time
from delayed_assert import expect, assert_expectations

class Login(Element):
    def __init__(self,driver):
        Element.__init__(self,driver)
        excel = ExcelReader()
        self.localeData = excel.getDataInHashMap("login", "LocaleData")
        self.testData = excel.getDataInHashMap("login", "LoginTestData")
        self.locators = excel.getDataInHashMap("login", "Locators")
        self.loginEmailData = excel.getDataInHashMap("login", "LoginEmailData")
        self.flag = False
        self.testBed = TestBed()
        self.loginType = ""

    def clearAppDataAndLaunchApp(self):
        self.testBed.clearAppDataAndLaunchApp2()

    def verifyUserLogin(self, loginType, country):
        emailId = self.loginEmailData[loginType]
        self.loginType =loginType

        print("loginType::::::" + loginType)
        print("EMAIL ID:::::::::" + emailId)
        isLoginSuccess = False
        if self.loginEmailData is None   or self.localeData is None :
             assert (False, "Login test failed as Login test data is null")
             return False
        self.clearAppDataAndLaunchApp()
        # self.is
        if (self.flag and "New" in loginType and "Private" not in loginType) :
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
            if (self.isLoginSuccess is False):
                 return False
            termsConditionCount = termsConditionFlow(termsConditionCount)
            isLoginSuccess = SoftAssertor.assertTrue(completeOnBoardingFlow(), "Error in completing Onboarding flow")
            if (isLoginSuccess is False)
                return False
            if ("EMPTYSTATE" not in loginType)
                Assert.assertTrue(changeUserGeoLocation(emailId.get(), country),
                              "Partial update user failed for loginType:::" + emailId.get() + " and user >>>"
                              + emailId.get())
            testBed.launchApp()
            return isLoginSuccess

    def isUserOnboardingWelcomeScreen(self):
        time.sleep(3)
        return not self.isElementByLocatorNotDisplayed(self.locators["LoginButton"])


    def verifyCarousel(self, count):
        carouselList = None
        carouselList = self.getListOfElementsByLocator(self.locators["CarouselButton"])
        for i in range(0,4):
            expect(self.isElementSelected(carouselList.get(i)),
                                        "Carousel bubble  not selected for carousel bubble number :::" + (i + 1))
            carouselBodyMessage = ""
            if (i == 0):
                continue
            else:
                expect(self.getElementText(self.locators["CarouselTitleText"])== self.localeData["CarouselTitleText".join(i + 1)],
                                          "CarouselTitleText not matched for carousel bubble number :::", (i + 1))
                carouselBodyMessage = self.getElementText(self.locators["CarouselBodyText"])

            expect(carouselBodyMessage == self.localeData["CarouselBodyText".join (i + 1)],
                                      "CarouselText not matched for carousel bubble number :::".join (i + 1))
            expect(self.isElementByLocatorNotDisplayed(self.locators["JoinNowButton"]) == False,
                                     "'SIGN UP' Button not displayed for carousel bubble number :::".join (i + 1))
            expect(self.isElementByLocatorNotDisplayed(self.locators["LoginButton"]) == False,
                                     "'LOG IN' Button not displayed for carousel bubble number :::".join (i + 1))

            self.screenSwipeRight(0.90, 0.3, 0.1, 0.3)

            count= count +1
        return count

    def navigateToSignInScreen(self):
        if "Existing" in self.loginType or "Existing":
                flag = self.click(self.locators["LoginButton"])
                expect(flag == True,
                        "Failed to click on 'LOG IN' button for login user type ::: ".join(self.loginType))
                self.verifyLoginWelcomeBackScreen()
        else:
            print("Else in navigateToSignInScreen")

    def verifyLoginWelcomeBackScreen(self):
        expect(self.isElementByLocatorNotDisplayed(self.locators["SignUpImage"])== False,
                "SignUp Image not seen on Welcome back login screen")
        expect(self.getElementText(self.locators["SignUpTitle"]) == self.localeData["SignUpTitleWelcomeBack"],
                "Welcome back login title mismatched")
        expect(self.getElementText(self.locators["SignUpBodyText"])== self.localeData["SignUpBodyText"],
                "Welcome back login subtitle mismatched")
        expect(self.isElementByLocatorNotDisplayed(self.locators["SignupGoogleButton"])==False,
                "GoogleSignUpButton not seen on Sign up screen")
        expect(self.isElementByLocatorNotDisplayed(self.locators.get("LoginFacebookButton"))==False,
                "LoginFacebookButton not seen on Sign up screen")
        expect(self.isElementByLocatorNotDisplayed(self.locators["EnterPartnerCodeLink"])== True,
                "'Enter partner code' link  button is seen on welcome back Sign up screen (i.e when users log out)")

        self.verifyLocalizationData("GoogleSignUpButton", "GoogleLoginButton", "GoogleLoginButton text not matched")
        self.verifyLocalizationData("LoginFacebookButton", "FacebookLoginButton", "FacebookLoginButton text not matched")
        self.verifyLocalizationData("ToggleUserLoginText", "ToggleUserSignUpText", "ToggleUserSignUpText text not matched")
        self.verifyLocalizationData("ToggleUserLoginButton", "SignUpLink", "SignUpLink text not matched")

    def verifyLocalizationData(self ,element,  locale,  message) :

        try :
            data = self.localeData[locale]
            commonEle = self.locators[element]
            if data == None :
                expect(False == True, "Locale data not added in localesheet for :::" .join(locale))
                return
            elif commonEle == None :
                expect(False ==True, "Locators data not added for :::" .join(element))
                return
            flag = True
        except :
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
        self.clickOnPrivacyPolicyLink()


    def clickOnTermsOfServiceLink(self):
        termsOfServiceWindow = expect(self.click(self.locators["TermsOfServiceButton"],
                                                       "Failed to click on Terms of Service link during new account creation for login user type :::"
                                                       + self.loginType)
        if (termsOfServiceWindow):
            expect(!isElementByLocatorNotPresent(locators.get("TermsOfServiceToolBar")),
                                     "TermsOfServiceToolBar not seen under AboutTermsOfService")
            time.sleep(5)
            expect(
            !isElementByLocatorNotDisplayed(constructXpathUsingText(localeData.get("TermsOfServiceText")))
             | | !isElementByLocatorNotDisplayed(
                constructXpathUsingContentDesc(localeData.get("TermsOfServiceText"))),
                  "TermsOfServiceContent " + "is empty under AboutTermsOfService")

                driver.navigate().back()

            // driver.navigate().back()
            sleep(2000)

            return true

    def clickOnPrivacyPolicyLink(self):
        // String
        testBedName = System.getProperty("TESTBEDNAME")
        boolean
        privacyPolicyWindow = expect(click(locators.get("PrivacyPolicyButton")),
                                                      "Failed to click on Privacy Policy link during new account creation for login user type :::"
                                                      + loginType)
        if (privacyPolicyWindow):
            sleep(2000)
            expect(!isElementByLocatorNotPresent(locators.get("PrivacyPolicyToolBar")),
                                     "PrivacyPolicyToolBar not seen under AboutPrivacyPolicy")
            if (deviceType.equalsIgnoreCase("iOS")):
                expect(!isElementByLocatorNotDisplayed(locators.get("PrivacyPolicyText")))
                else:
                expect(
                !isElementByLocatorNotDisplayed(constructXpathUsingText(localeData.get("PrivacyPolicyText")))
                 | | !isElementByLocatorNotDisplayed(
                    constructXpathUsingContentDesc(localeData.get("PrivacyPolicyText"))),
                      "PrivacyPolicyContent is empty under AboutPrivacyPolicy")

                    driver.navigate().back()

                // driver.navigate().back()
                sleep(2000)

            return true




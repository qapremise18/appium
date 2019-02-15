from util.ExcelReader import ExcelReader
from elementactions.Element import Element
from maintest.test.TestBed import TestBed
import time
class Login(Element):
    def __init__(self):
        Element.__init__(self)
        excel = ExcelReader()
        self.localeData = excel.getDataInHashMap("login", "LocaleData")
        self.testData = excel.getDataInHashMap("login", "LoginTestData")
        self.locators = excel.getDataInHashMap("login", "Locators")
        self.loginEmailData = excel.getDataInHashMap("login", "LoginEmailData")
        self.flag = False
        self.testBed = TestBed()


    def clearAppDataAndLaunchApp(self):
        self.testBed.clearAppDataAndLaunchApp2()

    def verifyUserLogin(self, loginType, country):
        emailId = self.loginEmailData[loginType]
        print("loginType::::::" + loginType)
        print("EMAIL ID:::::::::" + emailId)
        isLoginSuccess = False
        if self.loginEmailData is None   or self.localeData is None :
             assert (False, "Login test failed as Login test data is null")
             return False
        self.clearAppDataAndLaunchApp()
        if (self.flag and "New" in loginType and "Private" not in loginType) :
            assert (self.isUserOnboardingWelcomeScreen(), "User is not on onboarding Welcome screen")
            print("User is on onboarding Welcome screen")
            carouselCount = self.verifyCarousel()

        print("Clicking on Sign IN")
        flag = assert(self.navigateToSignInScreen(), "Unable to click on Navigate to sign in screen")
        if (self.flag is False):
            return False
        print("Started Login validation for -->" + loginType)
        list = ["NewGmailPublicUser","NewFBPublicUser","NewGmailPrivateUserCALISU","NewGmailSuperPrivateUserDREAMS",
                "NewGmailPrivateUserIOSPRIVATE","NewFBSuperPrivateUserDREAMS","NewFBPrivateUserCALISU",
                "NewGmailPrivateUserEMPTYSTATE","","","",""]
        if(loginType in list):
             isLoginSuccess = SoftAssertor.assertTrue(loginNewUser(loginType, true), "Unable to Login New User")
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
        return not self.isElementByLocatorNotDisplayed(self.locators.get("LoginButton"))


    def verifyCarousel(self, count):
            carouselList = None
            carouselList = getListOfElementsByLocator(locators.get("CarouselButton"))
        for i in range(0,4):
                self.assertTrue(isElementSelected(carouselList.get(i)),
                                        "Carousel bubble  not selected for carousel bubble number :::" + (i + 1))
             carouselBodyMessage = ""
            if (i == 0):
                SoftAssertor.assertTrue(isElementEnabled(locators.get("PremiseLogo")),
                                        "PremiseLogo not seen for carousel bubble number :::" + (i + 1))
                    carouselBodyMessage = getElementText(locators.get("CarouselBodyText"))

            else:
                SoftAssertor.assertEquals(getElementText(locators.get("CarouselTitleText")),
                                          localeData.get("CarouselTitleText" + (i + 1)),
                                          "CarouselTitleText not matched for carousel bubble number :::" + (i + 1))
                carouselBodyMessage = getElementText(locators.get("CarouselBodyText"))

            SoftAssertor.assertEquals(carouselBodyMessage, localeData.get("CarouselBodyText" + (i + 1)),
                                      "CarouselText not matched for carousel bubble number :::" + (i + 1))
            SoftAssertor.assertTrue(isElementEnabled(locators.get("CarouselImage")),
                                    "Carousel image not displayed for carousel bubble number :::" + (i + 1))
            SoftAssertor.assertTrue(!isElementByLocatorNotDisplayed(locators.get("JoinNowButton")),
                                     "'SIGN UP' Button not displayed for carousel bubble number :::" + (i + 1))
            SoftAssertor.assertTrue(!isElementByLocatorNotDisplayed(locators.get("LoginButton")),
                                     "'LOG IN' Button not displayed for carousel bubble number :::" + (i + 1))

            screenSwipeRight(0.90, 0.3, 0.1, 0.3)

        count= count +1
    return count


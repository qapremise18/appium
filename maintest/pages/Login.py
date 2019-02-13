from util.ExcelReader import ExcelReader
from elementactions.Element import Element
class Login(Element):
    def __init__(self):
        excel = ExcelReader()
        self.localeData = excel.getDataInHashMap("login", "LocaleData")
        self.testData = excel.getDataInHashMap("login", "LoginTestData")
        self.locators = excel.getDataInHashMap("login", "Locators")
        self.loginEmailData = excel.getDataInHashMap("login", "LoginEmailData")
        self.flag = False


    def verifyUserLogin(self, loginType, country):
        emailId = self.loginEmailData[loginType]
        print("loginType::::::" + loginType)
        print("EMAIL ID:::::::::" + emailId)
        isLoginSuccess = False
        if self.loginEmailData is None   or self.localeData is None :
             assert (False, "Login test failed as Login test data is null")
        return False
        clearAppDataAndLaunchApp()
        if (flag and "New" in loginType and "Private" not in loginType) :
            assertTrue(isUserOnboardingWelcomeScreen(), "User is not on onboarding Welcome screen")
            print("User is on onboarding Welcome screen")
            carouselCount = verifyCarousel(carouselCount)

        log.debug("Clicking on Sign IN")
        flag = SoftAssertor.assertTrue(navigateToSignInScreen(), "Unable to click on Navigate to sign in screen")
        if (self.flag is False):
            return false
        log.debug("Started Login validation for -->" + loginType)
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
                return false
            if ("EMPTYSTATE" not in loginType)
                Assert.assertTrue(changeUserGeoLocation(emailId.get(), country),
                              "Partial update user failed for loginType:::" + emailId.get() + " and user >>>"
                              + emailId.get())
            testBed.launchApp()
            return isLoginSuccess
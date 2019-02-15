import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Element:
    def __init__(self, driver):
        self.driver = driver

    def getMobileLocator(self,locator, identifier) :
            try :
                if (identifier == "id") :
                    return (By.ID,"joinNowButton")

            except :
                print("Failed to identify the locatorType:::" + locator + ". Error :::" + e.getMessage())

    def getElementByLocator(self, locator):
        element = None
        try:
            identifier = locator[0:locator.index("=")]
            locatorVal = locator[locator.index("=")+1:]
            print("identifier=",identifier,"=== locatorVal",locatorVal)
            element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((identifier,locatorVal)))
            print("Element found ::presence_of_element_located::with locator : " , locator)
        except :
            print(" Failed to find element even on Explicit wait using",sys.exc_info())
        return element


    def getElementText(self, locator):
        text = ""
        try :
            element = self.getElementByLocator(locator)
            text = element.text
            print("Actual Element text::: " ,text)
        except :
            print("Exception occured while getting element text for:::" + locator)
        return text


    def isElementByLocatorNotDisplayed(self, locator) :
        try :
            element = self.getElementByLocator(locator)
            if element.is_displayed():
                print("Element found and isDisplayed::: true")
                return False
            else :
                print("Element found BUT isDisplayed::: FALSE")
                return True
        except:
            print("This is intended exception : Element could not be located using locator::: " , locator," Error message:::" ,sys.exc_info())
            return True
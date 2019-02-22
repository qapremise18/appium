import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
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

    def getListOfElementsByLocator(self, locator):
        self.getElementByLocator(locator)
        return self.getElementsByLocator(locator)


    def getElementsByLocator(self, locator):
        element = []
        try:
            identifier = locator[0:locator.index("=")]
            locatorVal = locator[locator.index("=")+1:]
            print("identifier=",identifier,"=== locatorVal",locatorVal)
            # element =  self.driver.find_elements(identifier, locatorVal)
            element = self.driver.find_elements_by_class_name(locatorVal)
            print("getElementsByLocator size>>>",len(element))
            print("Element found ::presence_of_element_located::with locator : " , locator)
        except :
            print(" Failed to find element even on Explicit wait using",sys.exc_info())
        return element

    def screenSwipeRight(self, startX, startY,  endX,  endY) :
        try :
            print("screenSwipeRight TEST>>>>>>>>")
            # windowSize = self.driver.get_window_size()
            # actions = TouchAction(self.driver)
            # actions.press(windowSize["width"])*0.85)
            # actions.wait()
            # actions.move_to()
            # actions.release().perform()
            # .press(PointOption.point((int) ((windowSize.width) * 0.85), (int) ((windowSize.height) * 0.90)))
            # .waitAction(WaitOptions.waitOptions(Duration.ofMillis(2000)))
            # .moveTo(PointOption.point((int) ((windowSize.width) * 0.10), (int) ((windowSize.height) * 0.90)))
            # .release().perform()
            # print("Completed swiping right the screen ")
        except :
            print("Failed to screenSwipeRight the device screen due to :::",sys.exc_info())

    def click(self, locator) :
        try :
            mapElement = self.getElementByLocator(locator)
            if mapElement is not None :
                mapElement.click()
                time.sleep(1)
                print("Clicked on Element having locator:::".join(locator))
                return True
            else :
                print("Failed to click on element as element is NULL ::: Locator:::" + locator)
                return False
        except :
            print("Unable to click on element :::", locator)
        return False


    def constructXpathUsingText(self, text) :
        locator = "xpath=//*[@text=\"TEXT\"]"
        return locator.replace("TEXT",text.__str__())

    def isElementSelected(self, locator) :

        flag = False
        element = None
        element = self.getElementByLocator(locator)
        if element.is_selected() :
            flag = True
            print("Element is found and is selected using locator :::" , locator)
        else :
            flag = False
            print("Element is found and not selected using locator :::" , locator)
        return flag

    def isElementByLocatorNotPresent(self, locator):
        try:
            element = self.getElementByLocator(locator)
            print("Element is found in elementByLocatorNotPresent :::Locator ::" + locator)
            return False
        except :
            return True

    def constructXpathUsingContentDesc(self, text):
        locator = "xpath=//*[contains(@content-desc,'TEXT']"
        return locator.replace("TEXT", text.__str__())
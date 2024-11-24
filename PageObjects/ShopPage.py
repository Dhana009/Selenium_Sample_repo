from selenium.webdriver.common.by import By
from utilities.Selectors import Selectors
from selenium.webdriver.support.select import Select

from PageObjects.ConfirmPage import ConfirmPage

class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.selectors = Selectors(self.driver)  # Initialize Selectors here


    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//li/a[@class='nav-link btn btn-primary']")

    
    def getCardTitles(self):
        return self.selectors.Verify_Clickable(*ShopPage.cardTitle)

    def getCardFooter(self):
        return self.selectors.Verify_Clickable(*ShopPage.cardFooter)

    def checkOutItems(self):
        checkout_button = self.selectors.Verify_Clickable(*ShopPage.checkOut)
        return checkout_button

    def Confirm_page(self):
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
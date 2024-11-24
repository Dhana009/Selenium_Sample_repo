from selenium.webdriver.common.by import By
from utilities.Selectors import Selectors
from selenium.webdriver.support.select import Select

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver
        self.selectors = Selectors(self.driver)

    final_checkout_button = (By.XPATH,"(//button[@type='button'])[4]")
    country = (By.ID,"country")
    checkbox_click = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    submit_button_l = (By.CSS_SELECTOR,"[type='submit']")

    def final_checkout(self):
        return self.selectors.Verify_Clickable(*ConfirmPage.final_checkout_button)

    def enter_country(self):
        return self.selectors.Verify_Clickable(*ConfirmPage.country)

    def select_india(self):
        return self.selectors.verifyLinktextPresence("India")

    def checkbox(self):
        return self.selectors.Verify_Clickable(*ConfirmPage.checkbox_click)

    def submit_btn(self):
        return self.selectors.Verify_Clickable(*ConfirmPage.submit_button_l)


        
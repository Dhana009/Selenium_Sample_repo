import pytest
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage
import time

class Testone(BaseClass):

    @pytest.fixture(autouse=True)
    def setup_pages(self):
        """
        Setup fixture to initialize page objects.
        This fixture will be run before each test method.
        """
        self.homepage = HomePage(self.driver)  # Initialize homepage
        self.checkout_page = self.homepage.shop_page()  # Navigate to shop items
        self.confirm_page = self.checkout_page.Confirm_page()  # Navigate to checkout
        yield  # This ensures that the test will execute after the setup
    

    @pytest.mark.homepage
    def test_home_page_entry(self):
        log = self.getLogger()


        # Interact with homepage elements
        log.info('Homepage is loaded')
        self.homepage.first_name()
        log.info('First name is entered')

        self.homepage.email_locator()
        log.info('Email is entered')

        self.homepage.password()
        log.info('Password is entered')

        self.homepage.check_box().click()
        log.info('Check box is clicked')

        self.homepage.gender()
        log.info('Gender is clicked')

        self.homepage.employment_status().click()
        log.info('Employment status is clicked')

        self.homepage.date_of_birth()
        log.info('DOB is entered')

        self.homepage.submit_button().click()
        log.info('Submit button is clicked')

        # Assert success message
        assert "The Form has been submitted successfully!." in self.driver.page_source
        log.info('Successfully completed')

    @pytest.mark.smoke
    def test_shop_page(self):
        log = self.getLogger()

        self.homepage.shopItems().click()

        # Perform actions on checkout page
        log.info('Navigating to shop page')
        self.checkout_page.getCardTitles()
        log.info('Retrieved card titles')

        self.checkout_page.getCardFooter().click()
        log.info('Retrieved card footers')

        self.checkout_page.checkOutItems().click()  # Replace with an actual confirm page action
        log.info('Confirmation page actions completed')

        time.sleep(2)


    def test_confirm_page(self):
        log = self.getLogger()

        self.confirm_page.final_checkout().click()
        self.confirm_page.enter_country().send_keys('ind')
        self.confirm_page.select_india().click()
        self.confirm_page.checkbox().click()
        self.confirm_page.submit_btn().click()
        

        assert "Thank you! Your order will be delivered in next few weeks" in self.driver.page_source
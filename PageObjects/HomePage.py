from selenium.webdriver.common.by import By
from utilities.Selectors import Selectors
from selenium.webdriver.support.select import Select
from PageObjects.ShopPage import ShopPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.selectors = Selectors(self.driver)  # Initialize Selectors here

    # Locators
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email_loct = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender_loct = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")
    dob = (By.XPATH,"//input[@type='date']")
    empl_status = (By.XPATH,"//input[@type='radio' and @value='option1']")
    password_loct = (By.CSS_SELECTOR, "input[placeholder='Password']")

    shop_1 = "//li/a[text()='Shop']"

    first_name_lt = "dhanunjaya"
    email_lt = "dhanunjaya@gmail.com"
    password_lt = "dhanunjaya"
    gender_lt = "Female"
    dob_lt = "17-01-1999"

    # click on the shop button
    def shopItems(self):
        shop_button = self.selectors.verify_presence(By.XPATH,HomePage.shop_1)
        return shop_button

    def shop_page(self):
        shop_page = ShopPage(self.driver) #inheriting the shop page into this method without again no need to create another object in test
        return shop_page

    #click on the first name 
    def first_name(self):
        return self.selectors.Verify_Clickable(*HomePage.name).send_keys(HomePage.first_name_lt)

    def email_locator(self):
        #print(f"Debug: HomePage.email = {HomePage.email_loct}, type = {type(HomePage.email_loct)}")
        return self.selectors.Verify_Clickable(*HomePage.email_loct).send_keys(HomePage.email_lt)


    #click on the password
    def password(self):
        return self.selectors.Verify_Clickable(*HomePage.password_loct).send_keys(HomePage.password_lt)

    #check the box
    def check_box(self):
        return self.selectors.Verify_Clickable(*HomePage.check)

    #give the gender from dropdown
    def gender(self):
        #print(f"Debug: HomePage.gender = {HomePage.gender_loct}, type = {type(HomePage.gender_loct)}")
        return Select(self.selectors.Verify_Clickable(*HomePage.gender_loct)).select_by_visible_text(text=HomePage.gender_lt)

    #enter the employment status
    def employment_status(self):
        return self.selectors.Verify_Clickable(*HomePage.empl_status)

    #enter the date of birth
    def date_of_birth(self):
        return self.selectors.Verify_Clickable(*HomePage.dob).send_keys(HomePage.dob_lt)

    #click the submit button
    def submit_button(self):
        return self.selectors.Verify_Clickable(*HomePage.submit)




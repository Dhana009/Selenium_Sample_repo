import inspect
import logging
import pytest
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


class Selectors:

    def __init__(self,driver):
        self.driver = driver


    def verify_presence(self, custom,path):
        return WebDriverWait(self.driver, 10).until(
        expected_conditions.presence_of_element_located((custom, path)))

    def Verify_Clickable(self, custom,path):
        return WebDriverWait(self.driver, 10).until(
        expected_conditions.element_to_be_clickable((custom, path)))

    def Verify_visibility(self, custom,path):
        return WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located((custom, path)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        return sel.select_by_visible_text(text)

    def verifyLinktextPresence(self, text):
        return WebDriverWait(self.driver, 10).until(
        expected_conditions.element_to_be_clickable((By.LINK_TEXT, text)))


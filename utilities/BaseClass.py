import inspect
import logging
import pytest
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures('setup')
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName) #name given

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter) #format given

        logger.addHandler(filehandler) # filehandler object
        logger.setLevel(logging.DEBUG) #base level

        return logger


    
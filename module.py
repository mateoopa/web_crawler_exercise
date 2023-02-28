from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import traceback
import sys


class Selenium:

    def __init__(self):
        self.time = 10

        try:
            options = Options()
            options.add_argument('--headless')
            options.add_argument("--ignore-certificate-error")
            options.add_argument("--ignore-ssl-errors")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        except (Exception,):
            print(f'{traceback.format_exc()} {locals()}')
            self.quit_driver()

    def navigate(self, url: str, stop: bool):
        try:
            self.driver.get(url)
        except (Exception,):
            print(f'{traceback.format_exc()} {locals()}')
            self.quit_driver()

    def wfe(self, by: By, element: str, stop: bool, element_name: str = None):
        """

        Wait for element

        """
        try:
            WebDriverWait(self.driver, self.time).until(ec.presence_of_element_located((by, element)))
            return True
        except (TimeoutException, UnexpectedAlertPresentException) as e:
            if stop:
                print(f'{traceback.format_exc()} {locals()}')
                self.quit_driver()
            else:
                return False
        except (Exception,):
            if not stop:
                return False
            print(f'{traceback.format_exc()} {locals()}')
            self.quit_driver()

    def fe(self, multiple: bool, by: By, elements: str, stop: bool):

        try:
            Selenium.wfe(self, by, elements, stop)
            if multiple:
                return self.driver.find_elements(by, elements)
            else:
                return self.driver.find_element(by, elements)

        except (TimeoutException, NoSuchElementException) as e:
            if stop:
                print(f'{traceback.format_exc()} {locals()}')
                self.quit_driver()
            else:
                return False
        except (Exception,):
            if not stop:
                return False
            print(f'{traceback.format_exc()} {locals()}')
            self.quit_driver()

    def quit_driver(self):
        try:
            if self.driver:
                self.driver.quit()
        except (Exception,):
            print(f'{traceback.format_exc()} {locals()}')


class GetParam:

    def __init__(self):
        if len(sys.argv) == 3:
            self.start_url = str(sys.argv[1])
            self.depth = int(sys.argv[2])
        else:
            print('Please pass parameters in this order <start_url: string> <depth: number>')
            sys.exit(0)

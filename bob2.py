from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


class Bob:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        driver.get('https://demat.bankofbaroda.co.in/feedbackportal')
        driver.maximize_window()
        driver.implicitly_wait(10)
        domain = driver.find_element_by_id('txtUserIdMobNo')
        domain.send_keys(self.username)
        driver.implicitly_wait(10)
        password = driver.find_element_by_id('txtPassword')
        password.send_keys(self.password)
        driver.implicitly_wait(10)
        password.send_keys(Keys.ENTER)

    def feedback_selection(self):
        driver.implicitly_wait(10)
        feedback = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, 'btnFeedback'))).click()

    def fill_form(self):
        driver.implicitly_wait(10)
        try:
            Ebank = Select(driver.find_element_by_id(
                'selCustEbankingInterested'))
            Ebank.select_by_visible_text('Yes')
            Ebank = Select(driver.find_element_by_id('selCustEbankingIssue'))
            Ebank.select_by_visible_text('No')
        except:
            pass
        try:
            Mbank = Select(driver.find_element_by_id(
                'selCustMbankingInterested'))
            Mbank.select_by_visible_text('Yes')
            Mbank = Select(driver.find_element_by_id('selCustMbankingIssue'))
            Mbank.select_by_visible_text('No')
        except:
            pass
        try:
            atm = Select(driver.find_element_by_id('selCustAtmInterested'))
            atm.select_by_visible_text('Yes')
            atm = Select(driver.find_element_by_id('selCustAtmIssue'))
            atm.select_by_visible_text('No')
        except:
            pass

    def fill_comment(self):
        comment = driver.find_element_by_id('txtFeedBackComment')
        comment.send_keys('NA')

    def submit(self):
        driver.find_element_by_id('btnFeedbackSubmit').click()

    def close_drop(self):
        close_drop = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[3]/button'))).click()


papa = Bob('JC057841', 'Welcome@4')
papa.login()

while True:
    papa.feedback_selection()
    papa.fill_form()
    papa.fill_comment()
    papa.submit()
    papa.close_drop()

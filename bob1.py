from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


class Bob:
    Mbank_exist = False
    Ebank_exist = False
    Atm_exist = False

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        driver.get('https://demat.bankofbaroda.co.in/feedbackportal')
        driver.maximize_window()
        driver.implicitly_wait(8)
        domain = driver.find_element_by_id('txtUserIdMobNo')
        domain.send_keys(self.username)
        driver.implicitly_wait(8)
        password = driver.find_element_by_id('txtPassword')
        password.send_keys(self.password)
        driver.implicitly_wait(8)
        password.send_keys(Keys.ENTER)

    def feedback_selection(self):
        feedback = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, 'btnFeedback'))).click()

    def check_form(self):
        # Ebank
        try:
            Ebank_intrested = driver.find_element_by_id(
                'selCustEbankingInterested')
            Bob.Ebank_exist = True
        except:
            pass

        # Mbank
        try:
            Mbank_intrested = driver.find_element_by_id(
                'selCustMbankingInterested')
            Bob.Mbank_exist = True
        except:
            pass

        # ATM
        try:
            Atm_intrested = driver.find_element_by_id('selCustAtmInterested')
            Bob.Atm_exist = True
        except:
            pass

    def fill_form(self):
        if not Bob.Atm_exist and Bob.Mbank_exist and Bob.Ebank_exist:  # N N Y
            #Mbank = True
            try:
                Mbank_intrested = Select(driver.find_element_by_id(
                    'selCustMbankingInterested'))
                Mbank_intrested.select_by_visible_text('Yes')

                Mbank_issue = Select(
                    driver.find_element_by_id('selCustMbankingIssue'))
                Mbank_issue.select_by_visible_text('No')
                Mbank_exist = False
            except:
                pass

            #Ebank = False
            try:
                Ebank_intrested = Select(driver.find_element_by_id(
                    'selCustEbankingInterested'))
                Ebank_intrested.select_by_visible_text('Yes')

                Ebank_issue = Select(
                    driver.find_element_by_id('selCustEbankingIssue'))
                Ebank_issue.select_by_visible_text('No')
                Ebank_exist = False
            except:
                pass

        elif Bob.Atm_exist and Bob.Mbank_exist and Bob.Ebank_exist:  # N N N
            #Mbank = True
            try:
                Mbank_intrested = Select(driver.find_element_by_id(
                    'selCustMbankingInterested'))
                Mbank_intrested.select_by_visible_text('Yes')

                Mbank_issue = Select(
                    driver.find_element_by_id('selCustMbankingIssue'))
                Mbank_issue.select_by_visible_text('No')
                Mbank_exist = False
            except:
                pass

            #Ebank = False
            try:
                Ebank_intrested = Select(driver.find_element_by_id(
                    'selCustEbankingInterested'))
                Ebank_intrested.select_by_visible_text('Yes')

                Ebank_issue = Select(
                    driver.find_element_by_id('selCustEbankingIssue'))
                Ebank_issue.select_by_visible_text('No')
                Ebank_exist = False
            except:
                pass

            #Atm = False
            try:
                Atm_intrested = Select(
                    driver.find_element_by_id('selCustAtmInterested'))
                Atm_intrested.select_by_visible_text('No')

                Atm_issue = Select(
                    driver.find_element_by_id('selCustAtmIssue'))
                Atm_issue.select_by_visible_text('No')
                Atm_exist = False
            except:
                pass

        elif not Bob.Ebank_exist and Bob.Atm_exist and Bob.Mbank_exist:  # Y N N
            #Atm = True
            try:
                Atm_intrested = Select(
                    driver.find_element_by_id('selCustAtmInterested'))
                Atm_intrested.select_by_visible_text('Yes')

                Atm_issue = Select(
                    driver.find_element_by_id('selCustAtmIssue'))
                Atm_issue.select_by_visible_text('No')
                Atm_exist = False
            except:
                pass

            #Mbank = True
            try:
                Mbank_intrested = Select(driver.find_element_by_id(
                    'selCustMbankingInterested'))
                Mbank_intrested.select_by_visible_text('Yes')

                Mbank_issue = Select(
                    driver.find_element_by_id('selCustMbankingIssue'))
                Mbank_issue.select_by_visible_text('No')
                Mbank_exist = False
            except:
                pass

        elif not Bob.Mbank_exist and Bob.Ebank_exist and Bob.Atm_exist:  # N Y N
            #Ebank = True
            try:
                Ebank_intrested = Select(driver.find_element_by_id(
                    'selCustEbankingInterested'))
                Ebank_intrested.select_by_visible_text('Yes')

                Ebank_issue = Select(
                    driver.find_element_by_id('selCustEbankingIssue'))
                Ebank_issue.select_by_visible_text('No')
                Ebank_exist = False
            except:
                pass

            #Atm = False
            try:
                Atm_intrested = Select(
                    driver.find_element_by_id('selCustAtmInterested'))
                Atm_intrested.select_by_visible_text('No')

                Atm_issue = Select(
                    driver.find_element_by_id('selCustAtmIssue'))
                Atm_issue.select_by_visible_text('No')
                Atm_exist = False
            except:
                pass

        elif not Bob.Ebank_exist and not Bob.Atm_exist and Bob.Mbank_exist:  # Y N Y
            #Mbank = True
            try:
                Mbank_intrested = Select(driver.find_element_by_id(
                    'selCustMbankingInterested'))
                Mbank_intrested.select_by_visible_text('Yes')

                Mbank_issue = Select(
                    driver.find_element_by_id('selCustMbankingIssue'))
                Mbank_issue.select_by_visible_text('No')
                Mbank_exist = False
            except:
                pass

        elif Bob.Ebank_exist and not Bob.Atm_exist and not Bob.Mbank_exist:  # N Y Y
            #Ebank = True
            try:
                Ebank_intrested = Select(driver.find_element_by_id(
                    'selCustEbankingInterested'))
                Ebank_intrested.select_by_visible_text('Yes')

                Ebank_issue = Select(
                    driver.find_element_by_id('selCustEbankingIssue'))
                Ebank_issue.select_by_visible_text('No')
                Ebank_exist = False
            except:
                pass

        elif not Bob.Ebank_exist and Bob.Atm_exist and not Bob.Mbank_exist:  # Y Y N
            #Atm = True
            try:
                Atm_intrested = Select(
                    driver.find_element_by_id('selCustAtmInterested'))
                Atm_intrested.select_by_visible_text('Yes')

                Atm_issue = Select(
                    driver.find_element_by_id('selCustAtmIssue'))
                Atm_issue.select_by_visible_text('No')
                Atm_exist = False
            except:
                pass

        else:
            pass

    def fill_comment(self):
        driver.find_element_by_id('txtFeedBackComment').send_keys('NA')

    def submit(self):
        driver.find_element_by_id('btnFeedbackSubmit').click()

    def close_drop(self):
        close_drop = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[3]/button'))).click()


papa = Bob('JC057841', 'Welcome@4')
papa.login()

while True:
    papa.feedback_selection()
    papa.check_form()
    time.sleep(1)
    papa.fill_form()
    papa.fill_comment()
    papa.submit()
    papa.close_drop()
    time.sleep(1)

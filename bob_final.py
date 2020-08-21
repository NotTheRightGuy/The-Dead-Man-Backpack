from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()


class Bob:

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

    def check_exists_by_id(id):
        try:
            driver.find_element_by_id(id)
        except:
            return False
        return True

    def fill_form(self):
        Ebank_exists = Bob.check_exists_by_id('selCustEbankingInterested')
        Mbank_exists = Bob.check_exists_by_id('selCustMbankingInterested')
        Atm_exists = Bob.check_exists_by_id('selCustAtmInterested')
        print(Ebank_exists, Mbank_exists, Atm_exists)

        if Ebank_exists and Mbank_exists and Atm_exists:
            time.sleep(2)  # N N N
            Ebank = Select(driver.find_element_by_id(
                'selCustEbankingInterested'))
            Ebank.select_by_visible_text('No')
            Ebank = Select(driver.find_element_by_id('selCustEbankingIssue'))
            Ebank.select_by_visible_text('No')

            Mbank = Select(driver.find_element_by_id(
                'selCustMbankingInterested'))
            Mbank.select_by_visible_text('Yes')
            Mbank = Select(driver.find_element_by_id('selCustMbankingIssue'))
            Mbank.select_by_visible_text('No')

            atm = Select(driver.find_element_by_id('selCustAtmInterested'))
            atm.select_by_visible_text('No')
            atm = Select(driver.find_element_by_id('selCustAtmIssue'))
            atm.select_by_visible_text('No')

        if not Ebank_exists and Mbank_exists and Atm_exists:  # Y N N
            Mbank = Select(driver.find_element_by_id(
                'selCustMbankingInterested'))
            Mbank.select_by_visible_text('Yes')
            Mbank = Select(driver.find_element_by_id('selCustMbankingIssue'))
            Mbank.select_by_visible_text('No')

            atm = Select(driver.find_element_by_id('selCustAtmInterested'))
            atm.select_by_visible_text('Yes')
            atm = Select(driver.find_element_by_id('selCustAtmIssue'))
            atm.select_by_visible_text('No')

        if Ebank_exists and not Mbank_exists and Atm_exists:  # N Y N
            Ebank = Select(driver.find_element_by_id(
                'selCustEbankingInterested'))
            Ebank.select_by_visible_text('Yes')
            Ebank = Select(driver.find_element_by_id('selCustEbankingIssue'))
            Ebank.select_by_visible_text('No')

            atm = Select(driver.find_element_by_id('selCustAtmInterested'))
            atm.select_by_visible_text('No')
            atm = Select(driver.find_element_by_id('selCustAtmIssue'))
            atm.select_by_visible_text('No')

        if Ebank_exists and Mbank_exists and not Atm_exists:  # N N Y
            Ebank = Select(driver.find_element_by_id(
                'selCustEbankingInterested'))
            Ebank.select_by_visible_text('No')
            Ebank = Select(driver.find_element_by_id('selCustEbankingIssue'))
            Ebank.select_by_visible_text('No')

            Mbank = Select(driver.find_element_by_id(
                'selCustMbankingInterested'))
            Mbank.select_by_visible_text('Yes')
            Mbank = Select(driver.find_element_by_id('selCustMbankingIssue'))
            Mbank.select_by_visible_text('No')

        if not Ebank_exists and not Mbank_exists and Atm_exists:  # Y Y N

            atm = Select(driver.find_element_by_id('selCustAtmInterested'))
            atm.select_by_visible_text('Yes')
            atm = Select(driver.find_element_by_id('selCustAtmIssue'))
            atm.select_by_visible_text('No')

        if not Ebank_exists and Mbank_exists and not Atm_exists:  # Y N Y

            Mbank = Select(driver.find_element_by_id(
                'selCustMbankingInterested'))
            Mbank.select_by_visible_text('Yes')
            Mbank = Select(driver.find_element_by_id('selCustMbankingIssue'))
            Mbank.select_by_visible_text('No')

        if Ebank_exists and not Mbank_exists and not Atm_exists:  # N Y Y
            Ebank = Select(driver.find_element_by_id(
                'selCustEbankingInterested'))
            Ebank.select_by_visible_text('Yes')
            Ebank = Select(driver.find_element_by_id('selCustEbankingIssue'))
            Ebank.select_by_visible_text('No')

    def fill_comment(self):
        driver.find_element_by_id('txtFeedBackComment').send_keys('NA')

    def submit(self):
        driver.find_element_by_id('btnFeedbackSubmit').click()

    def close_drop(self):
        close_drop = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[3]/button'))).click()


def start(username, password):
    obj = Bob(username, password)
    obj.login()
    while True:
        obj.feedback_selection()
        obj.fill_form()
        obj.fill_comment()
        obj.submit()
        obj.close_drop()
        time.sleep(1)


start('Hs127469', 'Welcome@10')

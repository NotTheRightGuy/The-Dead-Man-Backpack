import requests
from bs4 import BeautifulSoup
import datetime
import os
import re
# import matplotlib.pyplot as plt

os.chdir('C:\\Users\XIV\\Desktop\\Covid Data')

today = datetime.date.today()
day_before = today - datetime.timedelta(1)

with open(str(day_before) + '.txt','r') as day_b:
    data = day_b.read()

number_datas = re.compile(r'\d+')
numbers_found = re.findall(number_datas,data)
total_active_cases_yesterday = int(numbers_found[2]) # Total Active cases Yesterday

day = today.strftime('%d %B %Y')
page = requests.get(r'https://www.worldometers.info/coronavirus/country/india/')
soup = BeautifulSoup(page.text, 'lxml')

numbers = soup.find_all('div',class_='maincounter-number')

total_cases = int(numbers[0].text.replace(",",""))
total_death = int(numbers[1].text.replace(",",""))
total_recovery = int(numbers[2].text.replace(",",""))
total_active = total_cases - total_recovery  # Total Active Cases today

increase_in_active_cases = total_active - total_active_cases_yesterday

with open(str(today)+'.txt','w') as file:
    file.write("""
Date:{}
-----------------------
Total Active Cases = {}
Total recoveries made = {}
Total number of death = {}
Increase in active case = {}
-----------------------
Total number of cases came so far = {}
""".format(day,total_active,total_recovery,total_death,increase_in_active_cases,total_cases))

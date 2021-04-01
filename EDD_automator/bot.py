from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import random
import unicodedata

okay_outcomes = ['No Decision', 'Pending', 'Not Hiring', 'No response from employer', 'Applied', 'Interview Date Set', 'Interviewed']
types_of_work = ['Crew Member', 'General Crew', 'Janitorial']
places = []
f = open('places.txt', 'r', encoding='utf-8')
name = f.readline()
while name:
    unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
    name.replace('\n', '')
    phone = f.readline()
    unicodedata.normalize('NFKD', phone).encode('ascii', 'ignore')
    phone.replace('\n', '')
    address = f.readline()
    unicodedata.normalize('NFKD', address).encode('ascii', 'ignore')
    address.replace('\n', '')
    places.append([name, phone, address])
    name = f.readline()
    name = f.readline()

f.close()

usednames = []
usedphones = []
f = open('usednames.txt', 'r', encoding='ascii')
line = f.readline()
while line:
    usednames.append(line)
    
f.close()

f = open('usedphones.txt', 'r', encoding = 'ascii')
line = f.readline()
while line:
    usedphones.append(line)
f.close()

pswd = input('enter password: ')

bot = webdriver.Firefox()
bot.set_page_load_timeout(10)

url = 'https://portal.edd.ca.gov/WebApp/Login?resource_url=https%3A%2F%2Fportal.edd.ca.gov%2FWebApp%2FHome'
uio_url = 'https://uio.edd.ca.gov/UIO/Pages/Public/ExternalUser/UIOnlineLandingPage.aspx?l=en'

bot.get(url)

bot.find_element_by_id('username').send_keys('rl.nguyen@outlook.com')

yes = input('Is the captcha filled out?')

if yes != 'n':
    bot.find_element_by_id('submitButton').click()

while (True):
    try:
        bot.find_element_by_id('password').send_keys(pswd)
        bot.find_element_by_id('loginSubmit').click()
        break
    except Exception as e:
        print(e)

bot.get(uio_url)

while (True):
    try:
        bot.find_element_by_id('contentMain_contentMain_ucNotifications_gvNotifications_lbNotificationFirstPart_0').click()
        sleep(.5)
        bot.find_element_by_xpath('//*[@id="contentMain_contentMain_ucNotifications_gvNotifications_lbNotificationFirstPart_0"]')
        break
    except Exception as e:
        print(e)


while (True):
    try:
        bot.find_element_by_id('contentMain_contentMain_ucFormCCA4581RegularDUACertificationQuestions_frmDE4581FullTime_prtDE4581FTQuestion1_ctl00_rblValue_1').click()
        bot.find_element_by_id('contentMain_contentMain_ucFormCCA4581RegularDUACertificationQuestions_frmDE4581FullTime_prtDE4581FTQuestion2_ctl00_rblValue_1').click()
        bot.find_element_by_id('contentMain_contentMain_ucFormCCA4581RegularDUACertificationQuestions_frmDE4581FullTime_prtDE4581FTQuestion3ESW_ctl00_rblValue_0').click()
        bot.find_element_by_id('contentMain_contentMain_ucFormCCA4581RegularDUACertificationQuestions_frmDE4581FullTime_prtDE4581FTQuestion4_ctl00_rblValue_1').click()
        bot.find_element_by_id('contentMain_contentMain_ucFormCCA4581RegularDUACertificationQuestions_frmDE4581FullTime_prtDE4581FTQuestion5_ctl00_rblValue_1').click()
        bot.find_element_by_id('contentMain_contentMain_ucFormCCA4581RegularDUACertificationQuestions_frmDE4581FullTime_prtDE4581FTQuestion6_ctl00_rblValue_1').click()
        bot.find_element_by_id('contentMain_contentMain_btnNext').click()
        break
    except Exception as e:
        print(e)

date = bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtDateOfContact_ctl00_txtDate')
type_of_work = bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtTypeOfWork_ctl00_txtValue')
employer_name = bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtEmployerAgencyName_ctl00_txtValue')
contact_type = Select(bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtContactType_ctl00_ddlValue'))
outcome_of_contact = Select(bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtOutcomeWorkInquiry_ctl00_ddlValue'))
phone_number = bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtPhoneFaxNumber_ctl00_txtValue')
address_1 = bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtAddress1_ctl00_txtValue')
city = bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtCity_ctl00_txtValue')
state = bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtOtherState_ctl00_txtValue')
postal_code = bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtPostalCode_ctl00_txtValue')
country = bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtCountry_ctl00_ddlValue')
additional_no = bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtISAdditionalWorkSerach_ctl00_rblValue_1')
additional_yes = bot.find_element_by_id('contentMain_contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtISAdditionalWorkSerach_ctl00_rblValue_0')
next_page = bot.find_element_by_id('contentMain_contentMain_btnNext')

while True:
    try:

        break
    except Exception as e:
        print(e)


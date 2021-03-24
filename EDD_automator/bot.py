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
    places.append([name, phone])
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
mob_url = 'https://uiom.edd.ca.gov/UIOM/Pages/Public/ExternalUser/UIOMobileLandingPage.aspx?l=en'

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

bot.get(mob_url)

while (True):
    try:
        bot.find_element_by_id('contentMain_gvNotifications_lbNotificationFirstPart_0').click()
        break
    except Exception as e:
        print(e)


while (True):
    try:
        bot.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[2]/table/tbody/tr/td/ol/li[1]/div/div[2]/span/label[2]').click()
        bot.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[2]/table/tbody/tr/td/ol/li[3]/div/div[2]/span/label[2]').click()
        bot.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[2]/table/tbody/tr/td/ol/li[4]/div/div[2]/span/label[1]').click()
        bot.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[2]/table/tbody/tr/td/ol/li[5]/div/div[2]/span/label[2]').click()
        bot.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[2]/table/tbody/tr/td/ol/li[6]/div/div[2]/span/label[2]').click()
        bot.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[2]/table/tbody/tr/td/ol/li[7]/div/div[2]/span/label[2]').click()
        bot.find_element_by_id('btnNext').click()
        break
    except Exception as e:
        print(e)

while (True):
    try:
        bot.find_element_by_id('btnAddWorkSearchRecord').click()
        break
    except Exception as e:
        print(e)

while (True):
    try:
        bot.find_element_by_xpath('//*[@id="contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtDateOfContact_ctl00_divDatePicker"]').click()
        sleep(3)
        with open('html.txt', 'w') as f:
            f.write(bot.page_source)
            f.close()

        table = bot.find_element_by_class_name('table-condensed')
        rows = table.find_elements_by_tag_name('tr')
        days_avail = []
        for i in rows:
            cols = i.find_elements_by_tag_name('td')
            for j in cols:
                class_name = str(j.get_attribute('class'))
                if class_name.find('day active') != -1 or class_name.find('day new') != -1:
                    days_avail.append(j)


        nameEmployer = places[random.randint(0, len(places))][0]
        phoneNum = places[random.randint(0, len(places))][1]
        while nameEmplyer in usednames:
            nameEmployer = places[random.randint(0, len(places))][0]
        while phoneNum in usedphones:
            phoneNum = places[random.randint(0, len(places))][1]

        type_of_work = bot.find_element_by_xpath('//*[@id="contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtTypeOfWork_ctl00_txtValue"]')
        employer = bot.find_element_by_xpath('//*[@id="contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtEmployerAgencyName_ctl00_txtValue"]')
        contact_type = Select(bot.find_element_by_xpath('//*[@id="contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtContactType_ctl00_ddlValue"]'))
        outcome_of_contact = Select(bot.find_element_by_xpath('//*[@id="contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtOutcomeWorkInquiry_ctl00_ddlValue"]'))

        days_avail[random.randint(0, len(days_avail))].click()
        outcome_of_contact.select_by_visible_text(okay_outcomes[random.randint(0, len(okay_outcomes))])
        type_of_work.send_keys(types_of_work[random.randint(0, len(types_of_work))])
        contact_type.select_by_visible_text('Phone')
        phone_input = bot.find_element_by_xpath('//*[@id="contentMain_ucRegularDUA4581WorkSearchRecordV2_frmFormWorkSearchInformation_prtPhoneFaxNumber_ctl00_txtValue"]').send_keys(phoneNum)
        employer.send_keys(nameEmployer)
        
        

        break
    except Exception as e:
        print(e)


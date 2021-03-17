from selenium import webdriver
from time import sleep

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
        sleep(1)
        table = bot.find_element_by_tag_name('datepicker-days')
        rows = table.find_elements_by_tag_name('tr')
        for i in rows:
            cols = i.find_elements_by_tag_name('td')
            for j in cols:
                print(j.getText())

        break
    except Exception as e:
        print(e)


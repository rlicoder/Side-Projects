from selenium import webdriver

bot = webdriver.Firefox()
bot.set_page_load_timeout(10)

bot.get('file:///c:/xampp/htdocs/txt.html')

table = bot.find_element_by_class_name('table-condensed')

rows = table.find_elements_by_tag_name('tr')

for i in rows:
    cols = table.find_elements_by_tag_name('td')
    for j in cols:
        print(j.text)

import re
from selenium import webdriver

for i in range(3355,3460):

    bot = webdriver.Firefox()

    site = 'https://naq20.kattis.com/standings?filter='
    site += str(i)

    bot.get(site)

    html = bot.page_source
    f = open("og.txt", "w")
    f.write(html)
    f.close()
    html = html.replace("\t", "")
    html = html.replace("\n","")
    html = html.replace(" ", "")
    f = open("out.txt", "w")
    f.write(html)
    f.close()

    names = re.findall('<div>.*?</div>', html)
    score = re.findall('<tdclass="totaltable-min-wrap.*?</td>', html)
    school = re.findall('Affiliation:.*?/h2>', html)

    school_name = school[0][12:-5]

    sname = open("schoolnames.txt", "a")
    team = open("teamnames.txt", "a")
    scores = open("scores.txt", "a")

    count = 0
    for i in names:
        if len(i) < 70:
            i = i.replace('<div>', '')
            i = i.replace('</div>', '')
            team.write(i + '\n')
        else:
            count += 1

    for i in range(0, len(score), 2):
        score[i] = score[i][51:]
        score[i] = score[i].replace('</td>', '')
        score[i+1] = score[i+1][51:]
        score[i+1] = score[i+1].replace('</td>', '')
        scores.write(score[i] + ' ' + score[i+1] + '\n')

    if len(names)-count != len(score)/2:
        print("TROUBLE at", school_name)

    for i in range(0, len(names)-count):
        sname.write(school_name + '\n')


    bot.quit()

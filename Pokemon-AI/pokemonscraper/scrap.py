from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://pokemondb.net/pokedex/all")

cookiesOk = driver.find_element_by_xpath("/html/body/div/div/div/p[2]/button")
cookiesOk.click();

pokedex = {}
f = open("pokedex.dat", "r")
for line in f:
    pokedex.add(line);

tableOfPokemon = driver.find_element_by_id("pokedex")
rows = tableOfPokemon.find_elements_by_tag_name("tr")

f = open("pokedex.dat", "a")
data = ""
for i in range(len(rows)):
    cells = rows[i].find_elements_by_tag_name("td")
    for j in range(len(cells)):
        if j == 1 and '\n' in cells[j].text:
            data += cells[j].text.split('\n')[0]
            data += ' '
            #print(cells[j].text.split('\n')[0], end=' ')
        elif j == 2 and '\n' in cells[j].text:
            data += cells[j].text.replace('\n', '/')
            data += ' '
            #print(cells[j].text.replace('\n', '/'), end=' ')
        else:
            data += cells[j].text
            data += ' '
            #print(cells[j].text, end=' ')
        #print(repr(cells[j].text), end=' ')
    data += '\n'
    if (data not in pokedex):
        f.write(data)
    #print(end='\n')






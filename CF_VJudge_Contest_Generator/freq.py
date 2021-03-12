f = open('tags.txt', 'r')

x = []
lines = f.readlines()

for line in lines:
    x.append([0, line.replace('\n', '')])


raw = open('final.csv', 'r')
lines = raw.readlines()
for i in x:
    for j in lines:
        if j.find(i[1]) != -1:
            i[0] += 1;

x.sort(reverse=True)
for i in x:
    print(i)

f.close()

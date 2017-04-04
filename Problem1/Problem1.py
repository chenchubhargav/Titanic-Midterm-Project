import re

titanic = open('titanic3.csv', 'r')
s = open('single.csv', 'w')
p = open('married.csv', 'w')
r = open('unknown.csv','w')
t = titanic
#print(t)

for line in t:
    l1 = line.rstrip()
    line = line.split(',')
    #print(l1)
    W = re.search(r'Miss.|Master.', l1)
    x = re.search(r'Mrs.|Mme.|Sir\s|Lady', l1)
    y = re.search(r'Mr.|Sir.|Count.', l1)
    if W:
        s.write(l1 + '\n')
        #print(line)
    elif x:
        p.write(l1 + '\n')
        #print (line)
    elif y:
        sibsp = line[6]
        if int(sibsp) >= 1:
            p.write(l1 + '\n')
        elif int(sibsp) == 0:
            r.write(l1 + '\n')
    else:
        r.write(l1 + '\n')
import re

t = open('titanic3.csv', 'r')
m = open('maiden.txt', 'w')
a = open('aka.txt', 'w')
am = open('akamaiden.txt', 'w')
for line in t:
    line = line.rstrip()
    line = line.split(',')
    w = re.findall(r'\((\w.+)\)|\s\(""(.*?\w\)")', line[3])
    x = re.findall(r'\s""(.*?)""', line[3])
    y = re.findall(r'\s\(""(.*?)""\)"', line[3])
    try:
        a.write(x[0] + '\n')
    except:
        print('no match')
    try:
        m.write(w[0][0] + '\n')
    except:
        print('no match')
    try:
        am.write(y[0] + '\n')
    except:
        print('no match')
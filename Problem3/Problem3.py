import re
t = open('titanic3.csv', 'r')
s = open('modtitanic.csv', 'w')

l = {}
for line in t:
    line = line.replace('"', '').strip()
    line = line.rstrip()
    line = line.split(',')
    try:
        if line[12] != '':
            try:
                if int(line[12]) <= 9:
                    line[12] = '0' + line[12]
                    l[line[3] + line[2]] = [line[12]]
                elif int(line[12]) >= 10:
                    l[line[3] + line[2]] = [line[12]]
            except:
                l[line[3] + line[2]] = [line[12]]
    except:
       print('Not Survived')
p = sorted(l.items(), key = lambda x:x[1])
for a in p:
    s.write(str(a[0]) + ',' + str(a[1]) + '\n')
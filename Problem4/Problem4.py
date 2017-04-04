
t = open('titanic3.csv', 'r')
s = open('modtitanic3.csv', 'w')

for line in t:
    line = line.rstrip()
    line = line.split(',')
    #print(line)
    try:
        if float(line[5]) < 13:
            line[5] = "Child"
            line = ','.join(line)
            #print(line)
            s.write(line + '\n')
        elif float(line[5]) < 20:
            line[5] = 'Teenager'
            line = ','.join(line)
            s.write(line + '\n')
        elif float(line[5]) < 56:
            line[5] = 'Adult'
            line = ','.join(line)
            s.write(line + '\n')
        elif float(line[5]) >= 56:
            line[5] = 'Senior'
            line = ','.join(line)
            s.write(line + '\n')
    except:
        line[5] = 'Unknown'
        line = ','.join(line)
        #print(line)
        s.write(line + '\n')
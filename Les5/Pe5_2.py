file = open('Kaartnummers.txt', 'r')
for lines in file:
    number, word = lines.split(',')
    print(lines[10:20].replace('\n',''),"BLAH BLAH BLAH", lines[0:6])
file.close()


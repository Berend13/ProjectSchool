file = open('hardlopers.txt','a')
dateInput = input('Date:')
timeInput = input('Time:')
nameInput = input('Name:')
file.write(dateInput)
file.write(', ')
file.write(timeInput)
file.write(', ')
file.write(nameInput)
file.write('\n')
file.close()

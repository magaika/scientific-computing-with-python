#Write a program to look for lines of the form:
#New Revision: 39772
#Extract the number from each of the lines using a regular expression
#and the findall() method. Compute the average of the numbers and
#print out the average as an integer.
fname = input('Enter file: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
import re
count = 0
summa = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    count += len(x)
    for number in x:
        y = int(number)
        summa += y
average = summa/count
print(int(average))

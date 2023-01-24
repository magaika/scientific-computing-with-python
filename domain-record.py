#This program records the domain name (instead of the address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    if line.startswith('From '):
        atpos = line.find('@')
        spacepos = line.find(' ', atpos)
        domain = line[atpos+1:spacepos]
        if domain not in counts:
            counts[domain] = 1
        else:
            counts[domain] += 1
print(counts)

#a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from 
#each email address, and print the dictionary.
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] += 1
print(counts)

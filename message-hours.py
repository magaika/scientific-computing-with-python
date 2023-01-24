#This program counts the distribution of the hour of the day for each of the messages.
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
        timepos = words[5]
        time = timepos[:2]
        if time not in counts:
            counts[time] = 1
        else:
            counts[time] += 1
import collections
odict = collections.OrderedDict(sorted(counts.items()))
for key, val in odict.items():
    print(key, val)

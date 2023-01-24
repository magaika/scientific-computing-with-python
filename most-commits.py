#print the person with the most commits
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
l = list()
for key, val in counts.items():
    l.append((val, key))
l.sort(reverse=True)
for key, val in l[:1]:
    print(val, key)

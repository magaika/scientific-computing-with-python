#to figure out who has the most messages in the file.
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
maximum = 0 
max_email = ''
for key in counts:
    if counts[key] > maximum:
        maximum = counts[key]
        max_email = key
print(max_email, maximum)

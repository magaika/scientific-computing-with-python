#program categorizes each mail message by which day of the week the commit was done
counts = dict()

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    #conditon1 = len(words) < 3 
    #condition2 = words[0] != 'From '
    if len(words) < 3 or words[0] != 'From': continue
    else:
        if words[2] not in counts:
            counts[words[2]] = 1
        else:
            counts[words[2]] += 1
print(counts)

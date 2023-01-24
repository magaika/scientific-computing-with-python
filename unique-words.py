#print a list of unique words in alphabetical order
filename =  input('Enter file: ')
fhand = open(filename)
ulist = []
for line in fhand:
    words = list(line.split())
    for word in words:
        if word not in ulist:
            ulist.append(word)
        else: continue
print(sorted(ulist))

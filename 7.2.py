#This program reads though a mbox file and prints out the average spam confidence.
filename =  input('Enter the file name: ')
try:
    fileopen = open(filename)
except:
    print('File cannot be opened: ', filename)
    exit()
total = 0
count = 0
for line in fileopen:
    if line.find('X-DSPAM-Confidence:') == -1: continue
    fnumber = float(line[20:])
    total = total + fnumber
    count = count + 1
avg = total/count
print('Average spam confidence: ', avg)
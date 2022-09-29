total = 0
count = 0
average = 0
while True:
    try:
        line = input("Enter a number: ")
        if line == 'done':
            break
        total = total + int(line)
        count = count + 1 
        average = total / count
    except:
        print("Invalid input")
print(total, count, average)

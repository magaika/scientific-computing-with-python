total = 0
count = 0
average = 0
largest = None
smallest = None
while True:
    try:
        line = input("Enter a number: ")
        if line == 'done':
            break
        total = total + int(line)
        count = count + 1 
        average = total / count
        if largest == None or line > largest:
            largest = line
        if smallest == None or line < smallest:
            smallest = line
    except:
        print("Invalid input")
print(total, count, average, largest, smallest)

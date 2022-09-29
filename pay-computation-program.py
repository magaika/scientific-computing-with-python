hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))
if hours > 40:
    pay = (hours - 40) * (rate * 1.5) + (40 * rate)
else:
    pay = hours * rate
print("Pay: ", pay)

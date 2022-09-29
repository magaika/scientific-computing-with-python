def computepay(hours, rate):
    if hours > 40:
        pay = (hours - 40) * (rate * 1.5) + (40 * rate)
    else:
        pay = hours * rate
    print("Pay: ", pay)
try:
    h = int(input("Enter Hours: "))
    r = int(input("Enter Rate: "))
    computepay(h, r)
except:
    print("Error, please enter numeric input")

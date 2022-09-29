def computegrade(score0):
    if 1.0 > score0 > 0.0:
        if score0 >= 0.9:
            print("A")
        elif score0 >= 0.8:
            print("B")
        elif score0 >= 0.7:
            print("C")
        elif score0 >= 0.6:
            print("D")
        elif 0.0 < score0 < 0.6:
            print("F")
    else: 
        print("Bad score")

try:
    score = float(input("Enter score: "))
    computegrade(score)
except:
    print("Bad score")

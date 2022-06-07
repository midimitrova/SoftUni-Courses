degrees = float(input())

if degrees >= 26 and degrees <= 35:
    print("Hot")
elif degrees >= 20.1 and degrees <= 25.9:
    print("Warm")

elif degrees >= 15.00 and degrees <= 20.00:
    print("Mild")

elif degrees >= 12.00 and degrees <= 14.9:
    print("Cool")
elif degrees >= 5.00 and degrees <= 11.9:
    print("Cold")
else:
    print("unknown")
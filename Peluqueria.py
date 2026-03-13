llegada = int(input("Please enter your appointment time: "))
morning_shift = range(6,12)
afternoon_shift = range(12,18)
night_shift = range(18,22)
if llegada in morning_shift:
    print("Morning shift")
elif llegada in afternoon_shift:
    print("Afternoon shift")
else:
    print("Night shift")
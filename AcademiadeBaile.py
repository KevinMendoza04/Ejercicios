info = int(input("How many classes have you attended?: "))
if info < 5:
    print("Low attendance.")
elif 5 <= info <= 8:
    print("Middle attendance.")
elif info >= 9:
    print ("High attendance.")
else:
    print("No attendance information entered.")
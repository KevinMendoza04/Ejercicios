edad = int(input("Enter your age: "))

if edad < 13:
    print("You are under aged and cannot subscribe to the Gym membership.")
elif 13 <= edad <= 17:
    print("Juvenil Class.")
elif 18 <= edad <= 59:
    print("General Class.")
else:
    print("Senior Class")
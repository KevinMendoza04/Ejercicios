try:
    edad = int(input("Enter your age: "))
    if edad < 12:
        print("Movie ticket price: $8000.")
    elif 12 <= edad <= 59: 
        print("Movie ticket price: $12000.")
    else:
        print("Movie ticket price: $9000.")
except ValueError:
    print("Invalid input.")
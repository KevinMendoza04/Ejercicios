categoria_low = 0
categoria_middle = 0
categoria_high = 0


for i in range (5):
    print("Welcome to the gym! Lets get you registered.")
    nombre = input("Enter your name: ")
    dias_asistidos = int(input("How many days of this week you came the gym?: "))
    minutos_promedio = int(input("How many minutes per day?: "))
    if dias_asistidos < 3:
        categoria_low += 1
        print("Low commitment.")
    elif 3 <= dias_asistidos <= 4:
        categoria_middle += 1
        print("Middle commitment.")

    else:
        categoria_high += 1
        print("High commitment.")


print("\n___ Final Report ___")
print(f"For Low category we have {categoria_low} people.")
print(f"For Middle category we have {categoria_middle} people.")
print(f"For High category we have {categoria_high} people.")  
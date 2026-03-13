unahora = 5000
try:
    horas = int(input("How many hours did you park?: "))
    if horas == 1:
            print("Total cost is: $5000.")
    elif horas > 1:
            total_cost = unahora + (horas -  1) * 3000
            print(total_cost)
except ValueError:
    print("Invalid input.")

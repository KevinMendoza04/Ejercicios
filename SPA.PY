Servicio1 = "massage"
servicio2 = "facial"
servicio3 = "manicure"
service = input("What service would you like to book?: ").lower()
if service in [Servicio1, servicio2, servicio3]:
    print (f"Your {service} service has been confirmed. ")
else:
    print("That service does not exist, try again.")     
computer_price = float(input("Ile kosztuje komputer? "))
car_price = float(input("Ile kosztuje samochód? "))
bike_price = float(input("Ile kosztuje rower? "))

if computer_price > car_price:
    print("Komputer jest droższy od samochodu")
else:
    print(" Samochód jest droszy od komputera")

if bike_price < computer_price:
    print("Rower jest droższy od komputera")
else:
    print("Komputer jest droższy od rowera")

if car_price == bike_price:
    print(" Samochód i rower kosztują tyle samo")
else:
    print("Samochód i rower nie kosztują tyle samo")
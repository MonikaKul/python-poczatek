number = int(input("Podaj liczbę parzystą: "))
try_number = 1
while try_number < 10 and number % 2 != 0:
    number = int(input("Podaj kolejną liczbę: "))
    try_number += 1
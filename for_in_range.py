phone_number = input("Podaj numer telefonu: ")
for digit in range(10):
    digit_times_in_number = phone_number.count(str(digit))
    print(f"Cyfra {digit} występuje {digit_times_in_number} razy")
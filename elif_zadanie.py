print("Kalkulator lokaty -> 1, kalkulator kredytowy -> 2", sep="\n")
option = input("Wybierz opcję: ")

if option == "1":
    print("Klalkulator kredytowy")
    initial_value_input = input("Jaką kwotę wpłaciłeś? ")
    initial_value = int(initial_value_input)
    percentage_input = input("Jaki procent? ")
    percentage = int(percentage_input)
    years_input = input("Ile lat? ")
    years = int(years_input)

    final_value = initial_value * (1 +percentage/100)**years
    print(f" Po {years} latach twoja lokata będzie warta {final_value:.2f}")

elif option == "2":
    loan_amount = int(input("Jaka jest kwota kredytu? "))
    interest_rate = float(input("Jakie jest oprocentowanie? "))
    own_contibution = int(input("Jaka jest wartość wkładu własnego? "))
    years = int(input("Ile lat? "))
    monthly_income = int(input("Miesięczny  przychód? "))
    monthly_expenditures = int(input("Miesięczne wydatki? "))
    installment_value = (loan_amount * interest_rate / 100) / 12 + (loan_amount / (years * 12))
    available_money = monthly_income - monthly_expenditures
    property_value = loan_amount + own_contibution
    own_contribution_part = own_contibution / property_value
    money_over_installment = available_money - installment_value
    if own_contribution_part >= 0.2 and money_over_installment >= 1000:
        print("Możes wziąć kredyt")
    elif own_contribution_part >= 0.1 and money_over_installment >= 2000:
        print("Możesz wziąć kredyt")
    else:
        print("Nie możesz wziąć kredytu")
else:
    print(f"Nie ma takiej opcji {option}")


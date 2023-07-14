loan_amount = int(input("Jaka jest kwota kredytu? "))
interest_rate = float(input("Jakie jest oprocentowanie? "))
own_contibution = int(input("Jaka jest wartość wkładu własnego? "))
years = int(input("Ile lat? "))
monthly_income = int(input("Miesięczny  przychód? "))
monthly_expenditures = int(input("Miesięczne wydatki? "))
installment_value = (loan_amount * interest_rate / 100) / 12 + (loan_amount /(years * 12))
available_money = monthly_income - monthly_expenditures
property_value = loan_amount + own_contibution
own_contribution_part = own_contibution / property_value
money_over_installment = available_money - installment_value
mathing_higher_own_part = own_contribution_part >= 0.2 and money_over_installment >= 1000
mathing_lower_own_part = own_contribution_part >= 0.1 and money_over_installment >= 2000

if mathing_higher_own_part or mathing_lower_own_part:
    print("Możesz wziąć kredyt")
else:
    print("Nie możesz wziąć kredytu")
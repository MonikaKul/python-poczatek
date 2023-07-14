grades = []
grades_input = input("Podaj kolejną ocenę albo zakończ 'X': " )
while grades_input != 'X':
    grade= int(grades_input)
    grades.append(grade)
    grades_input = input("Podaj kolejną ocenę albo zakończ 'X': ")

grades_sum = 0
for grade in grades:
    grades_sum += grade
average = grades_sum/len(grades)
print(f"Twoja średnia wyniesie {average:.2f} ")
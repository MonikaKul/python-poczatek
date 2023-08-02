class Student:
    def __init__(self):
        self.first_name = "Monika"
        self.last_name = "Kulas"
        self.age = 100
def run_example():
    student=Student()
    #print(student.first_name)
    #print(student.last_name)
    #print(student.age)
    student.first_name = "Jan"
    student.last_name = "Kowalski"
    student.age = 99
    print(student.first_name)
    print(student.last_name)
    print(student.age)

if __name__ == '__main__' :
    run_example()
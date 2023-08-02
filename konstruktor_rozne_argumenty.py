class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

def print_student(student):
    print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}" )

def run_example():
    student = Student(first_name = "Ola", last_name = "Nowak")
    print_student(student)
    other_student = Student(first_name = "Kasia", last_name = "Kowalska")
    print_student(other_student)

if __name__ == '__main__':
    run_example()
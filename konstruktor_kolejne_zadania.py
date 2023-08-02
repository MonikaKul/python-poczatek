import random

class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

def print_student(student):
    print(f" Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")

def promoted_student(student):
    student.promoted = True

def run_example(student):
    student = Student(first_name = "Ola", last_name = "Nowak")
    print(student)
    other_student = Student("Bazyl", "Kowalski")
    print(other_student)

    promoted_student(student)
    print(student)

if __name__ = '__main__':
    run_example()
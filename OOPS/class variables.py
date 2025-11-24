class Student:

    class_year = 2024
    student_number = 28

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.student_number += 5

student1 = Student("Kaustubh",19)

# print(student1.name)
# print(student1.age)
# print(Student.class_year)
# print(Student.student_number)

print(f"{student1.name} is {student1.age} years old and is studying in LPU with passing year {Student.class_year} and he has {Student.student_number} Classmates")

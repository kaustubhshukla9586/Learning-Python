class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        total = 0
        for i in range(self.marks):
            total += i
        avg = total / len(self.marks)
        return avg
    def grade(self):
        if self.average() >= 85:
            print("Grade: A")
        elif self.average() >= 70:
            print("Grade: B")
        elif self.average() >= 55:
            print("Grade: C")
        else:
            print("Grade: D")
    def consistent(self):
        for i in self.marks:
            for j in self.marks:
                if i > j:
                    max = i
                    break
        for i in self.marks:
            if j in self.marks:
                if i < j:
                    min = i
                    break
        if (max-min) <= 20:
            return True
        else:
            return False

    def status(self):
        for i in self.marks:
            if i < 40:
                return "Fail"
            else:
                return "Pass"

name = list(map(str,input("Name: ").split()))
marks = list(map(int,input("Marks: ").split()))

for i in range(len(marks)-1):
    P = Student(name[i],marks[i])
    P.grade()
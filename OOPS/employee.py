class Employee:
    def __init__(self,employee_id,name,salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
    def allowance(self):
        hra = (20/100) * self.salary
        da = (10/100) * self.salary
        return hra + da
    def gross_salary(self):
        return self.salary + self.allowance()
    def tax(self):
        if self.gross_salary()>=50000:
            tax = (10/100) * self.gross_salary()
            return tax
        else:
            tax = (5/100) * self.gross_salary()
            return tax
    def net(self):
        return self.gross_salary()-self.tax()
    def display(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, ")
        print(f"Basic Salary: {self.salary}, Tax: {self.tax()}")
        print(f"Net Salary: {self.net()}")
        print()
        print()

employee_id = list(map(int,input("Enter Id: ").split()))
name = list(map(str, input("Name: ").split()))
salary = list(map(int,input("Salary: ").split()))
print()

for i in range(len(employee_id)):
    d = Employee(employee_id[i],name[i],salary[i])
    d.display()
0


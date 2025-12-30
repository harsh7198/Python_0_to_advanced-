# Defien a Employee class with attributes role , department & salary , this class also has Shoedetails()
# create an engineer class that inherits properties from employee & has additional attribute : name & age

class Employee:
    def __init__ (self , role , dept , salary):
        self.role = role
        self.dept = dept
        self.salary = salary   

    def Showdetails(self):
        print("Role = ", self.role)
        print("Dept = ", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self,name,age ):
        self.name = name 
        self.age = age 
        super().__init__("Engineer","IT", 75000)
        

# e1 = Employee("Accountant", "Finanace", 60000)
# e1.Showdetails()

engg1 = Engineer("Raghav", 19)
engg1.Showdetails()
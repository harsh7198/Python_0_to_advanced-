# create a student class that takes name & marks of three subjects as argument in constructor
# create a method for print avarage  

class Student: 
    def __init__(self, name , marks) :
        self.name = name
        self.marks = marks 
    @staticmethod # do not required self references 
    def greeting():
        print("Thanks you ! visit again.")
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,",self.name , "Your avg score is :", sum/3)

s1 = Student("Tony", [99,98,97])
s1.get_avg()
s1.greeting()
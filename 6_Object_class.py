class Student :
    # default construtor 
    def __init__(self):
        pass # nor run bcoz parameter not matched 
    # parameterized constructor , value more than self 
    def __init__(self, fullname, marks): # self is important 
        self.name = fullname
        self.marks = marks
        print("Adding New Student..")

s1 = Student("Harsh", 88)
print(s1.name , s1.marks) # harsh

s2 = Student("Arjun", 99)
print(s2.name , s2.marks )
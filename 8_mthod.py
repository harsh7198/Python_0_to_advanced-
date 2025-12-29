class Student :
    collage_name = "SPEC"  
       
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("Adding New Student..")

    def hello(self):
        print("Welcome !",self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Harsh", 88)
s1.hello()
print(s1.get_marks())


class Student :
    def __init__(self, phy , chem , math):
        self.phy = phy
        self.chem = chem 
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
    # percentage (simple way)
    # def calc_percentage(self):
    #    self.percentage = str((self.phy + self.chem + self.math)/3) + "%" 

    # use of property decorator 
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%" 
stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 52 # suppose change the marks
# stu1.calc_percentage()
print(stu1.percentage) # simple way 



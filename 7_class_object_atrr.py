class Student :
      collage_name = "SPEC" # same for all 
      name = "Anonymous" # class attribute
      def __init__(self, fullname, marks):
      
        self.name = fullname # different from anyone
        self.marks = marks
        print("Adding New Student..")

s1 = Student("Harsh", 88)
print(s1.name , s1.marks) # harsh

s2 = Student("Arjun", 99)
print(s2.name , s2.marks )

print(Student.collage_name) # object precidence higher than class attribute


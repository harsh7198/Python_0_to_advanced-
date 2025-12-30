class Person: 
    name = "someone"

    # def changename(self , name):
    #     Person.name = name
    #     # self.__class__.name = "Harsh"

    @classmethod # directly change class attribute
    def changename(cls, name):
        cls.name = name

p1 = Person()
p1.changename("Harsh suradkar")
print(p1.name)
print(Person.name)
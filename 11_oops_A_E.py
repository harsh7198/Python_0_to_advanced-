# Abstraction and Encapsulation 
# Abstarction : Hiding the implementation details of a class and only showing the essential feature to the user 
# Encapsulation : Wrapping data and function into a single unit 

class car : 
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print('Car started...')

car1 = car()
car1.start()
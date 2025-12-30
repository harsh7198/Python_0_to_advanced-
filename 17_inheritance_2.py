# multi_level inheritnace
class car : 
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(Toyotacar):
    def __init__(self, type):
        self.type = type
    

car1= Fortuner("Diesel")
print(car1.type)
car1.start()
class car : # single inheritance
    colour = "black"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("Fortuner")
car2 = Toyotacar("Camry")

print(car1.name)
print(car1.start())
print(car1.colour)
    
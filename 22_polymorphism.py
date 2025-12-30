# print(1+2) # perform addition 
# print("harsh" + "Suradkar") # concatination of strings 
# print([1,2,3] + [4,5,6]) # merge the list 

class Complex: 
        def __init__(self, real , img):
                self.real = real
                self.img = img 

        def Shownumber(self):
                print(self.real,"i +",self.img,"j")

        def __add__(self , num2):
                newReal = self.real + num2.real
                newImg = self.img + num2.img 
                return Complex(newReal, newImg)
        
        def __sub__(self , num2):
                newReal = self.real - num2.real
                newImg = self.img - num2.img 
                return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.Shownumber()

num2 = Complex(4,6)
num2.Shownumber()

num3 = num1 + num2
num3.Shownumber()

num3 = num1 - num2
num3.Shownumber()
class Account : 
    def __init__(self, acc_no , password):
        self.acc_no = acc_no
        self.__password = password # password is private , not to access 

    def reset_password(self):
        print(self.__password)

acc1 = Account("12345", "ABCDE")
print(acc1.acc_no)
print(acc1.reset_password())
# print(acc1.password)
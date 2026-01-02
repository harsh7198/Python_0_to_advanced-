print("---Welcome to FIZZ_BUZZ Game ---")
num = int(input("Enter a Number : "))


for i in range(1,num):
        if i %3==0:
            print("FIZZ")

        elif i %5==0:
            print("BUZZ")

        elif (i %5==0 and i %3==0):
            print("FIZZ BUZZ")

        else :
            print(i)

    
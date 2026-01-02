n = int(input("Enter a number: "))

if 10 <= n % 100 <= 13:
    print(str(n) + "th")
elif n % 10 == 1:
    print(str(n) + "st")
elif n % 10 == 2:
    print(str(n) + "nd")
elif n % 10 == 3:
    print(str(n) + "rd")
else:
    print(str(n) + "th")

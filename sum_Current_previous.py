num = int(input("Enter number of terms : "))
previous_number = 0 
for i in range (1,num):
    x_sum = previous_number + i 
    print("Current Number", i, "Previous Number ", previous_number, " Sum: ", x_sum)
    previous_number = i 
num = int(input("enter the number"))  # here, we converted int because if not the entered number will be stored as
factorial = 1  # this is to initialize the variable if we take 0 we wil get output as 0 as 0* anything is 0

if num < 0:
    print("Really EggHead factorials are always positive")
elif num == 0:
    print("Don't you know the basic Stuff, 0! = 1")

else:
    for i in range(num, 0, -1):  # from num to 0 and -1 is to decrement
        factorial = factorial * i  # we need to multiply in order to get factorial
        print(factorial)
print("Want to book tickets for travelling")
travelling = input()



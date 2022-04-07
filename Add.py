# adding two numbers

# num1 = input("Enter 1st number to add")  # we use built in function input
# num2 = input("Enter 2nd number to add")

# sum = int(num1) + int(num2)  # since the input() function return as string data type, we need to convert to (int)
# print("Solution")
# print(sum)

# addition in a single statement

# print('The sum is %.1f' % int((input('Enter first number: ')+int((input('Enter second number: '))) 

a =int(input("Enter a number"))
if a <0:
   print("enter a postive number")
else:  
 sum = 0
 while(a>0):
  sum +=a
  a -=1     
print(sum)
print("Enter two numbers, to print inbetween prims")
prime_upper = int(input("Enter first number"))
prime_lower = int(input("Enter second number"))

for num in range(prime_upper, prime_lower +1):
    if num>1:
       for i in range(2,num):
          if (num%i)==0:
             break
       else:
           print(num)   
       
      
# prime = int(input("Enter a number to check it is prime or not"))
# if prime<0:
#    print("should be positive")
# elif prime==1:
#    print("should be greater than one")
# else:
#    if prime >1:
#     for i in range(2, prime):
#        if (prime%i)==0:
#           print("Not a prime number")
#           break
#     else:
#           print("It is a prime number")  

                  
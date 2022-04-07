# Method 1
# n = int(input("enter how many numbers"))
# first= 0
# second =1
# for i in range(n):
#     print(first)
#     temp = first
#     first = second
#     second = temp+second
 
##### Method 2  
# nterms = int(input("How many terms? "))
# n1, n2 = 0, 1
# count = 0
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)#0              
#        nth = n1 + n2 #1
#        n1 = n2
#        n2 = nth
#        count =count + 1

# Method 3(using function)
"""def feb(n):
   a,b = 0,1
   for i in range(n):
     a,b = b,a+b
   return a

print(feb(6))"""





















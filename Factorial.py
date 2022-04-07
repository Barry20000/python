#using recursion 
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
        
# print(fact(5))

#####################################.
















# # using for loop

# def fact(n):
#  fa = 1
#  for i in range(1, n+1):
#   fa = fa * i
#  return fa

# print(fact(5))














#####################################
# using while loop
def factorial(n):
  if n < 0:
      return 0
  elif n==0 or n==1:
      return 1
  else:
      fact = 1
      while(n>1):
          fact *=n
          n -=1
      return fact
 
print(factorial(-1))  



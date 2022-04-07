# Leap_number = int(input("ENTER A YEAR TO CHECK IF ITS A LEAP YEAR"))

# if (Leap_number % 4) == 0:
#  if (Leap_number % 100) == 0:
#      if (Leap_number % 400) == 0:
#          print("{0} is a leap year".format(Leap_number))
#      else:
#          print("{0} is not a leap year".format(Leap_number))         
#  else: 
#    print("{0} is a leap year".format(Leap_number))
# else:
#  print("{0} is not a 20 leap year".format(Leap_number))



def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print(is_leap(int(input())))



















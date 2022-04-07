# Demonstration of built in functions(and and any)
# people = ["sonia", "sandy", "sunday"]
# check_condition = any([item[0] == 's' for item in people])  # you may not use [] these brackets, they are only used,
# check_condition2 = all([item[0] == 's' for item in people])  # if you want to store and use for list later
# nums = [2, 4, 6, 8, 9, 10]

# check_condition3 = any(num % 2 == 0 for num in nums)
# check_condition4 = all(num % 2 == 0 for num in nums)

# print(check_condition)
# print(check_condition2)
# print(check_condition3)
# print(check_condition4)

# squar = lambda num : num **10
# add = lambda a,b: a+b
#
# print(squar(2))
# print(add(90,220))
#
# print (squar.__name__)


# def make_noise():
#    return  "THE CROWD GOES WILD"

# result = make_noise()
# print(result)


# print even number in list using function
def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result

print(generate_evens())


# total odd numbers

# def sum_of_odd(numbers):
#     total =0
#     for num in numbers:
#       if num % 2!=0:
#           total += num
#     return total
#
#
# print(sum_of_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))

# def name (first, second):
#     print(f"{first} says hello to {second}")
#
# names = {"first" : "colt", "second" :"rusty"}
# name(first="barry", second ="harry")
#

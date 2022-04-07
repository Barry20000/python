for i in range(2000):
    num = i
    result = 0
    length_of_nums = len(str(i))
    while(i != 0):
      n = i % 10
      result = result + n ** length_of_nums
      i = i //10
    if num == result:
     print(num)


   
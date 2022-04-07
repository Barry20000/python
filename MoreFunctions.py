for i in range(1001):
    num = i
    result =0
    length = len(str(i))

    while (i>0):
        first_isolatation = i%10
        result = result+ first_isolatation**length
        second_isolatation = i//10

        if first_isolatation == num:
            print(num)

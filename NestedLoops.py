print("Want to book tickets for travelling")
travelling = input()

while travelling == 'yes' or 'no':

    num = int(input("Enter how many people want to travel"))

    for num in range(1, num + 1):
        name = input("name")

        age = input("Age")

        sex = input("sex")

        print(name)
        print(age)
        print(sex)

        travelling = input("for got someone")


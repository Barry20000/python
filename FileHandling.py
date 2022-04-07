# writing and creating and reading a file (remember you can create a file by both 'x' and 'w' only difference is by using x you will get error if the file already exits)
file = open("E:\Work\Coding\Python\Barry.txt" ,'w')
file.write("Damn the Data is gone. because you have overwritten it")
file = open("E:\Work\Coding\Python\Barry.txt" ,'r')
print(file.read())
file = open("E:\Work\Coding\Python\creating.txt" ,'x')
file.write("X- is used to create a new file")
file.close()


# deleting a file

import os

if os.path.exists("E:\Work\Coding\Python\dude.txt"):
    os.remove("E:\Work\Coding\Python\Barry.txt")
else:
    print("File doesnt exists")

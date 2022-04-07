class comment:
    def __init__(self,username,text,likes=0):
        self.username = username
        self.text = text
        self.likes = likes 
        
c = comment("davey123","lol you'r silly")
print(c.username,c.text,c.likes)
                                                                                                                                            
# class Person: 
#     def display(self):
#         print("Hello")
        
# person1 = Person()  
# person1.display()      

######Using inti Method######
# class parrot:
#     def __init__(self,name,age):
#         self.peru= name
#         self.vayasu=age
        
# now = parrot("lucky","3")
# prasad = parrot("Maw","10") 

# print(now.peru, now.vayasu)        
# print(prasad.peru,prasad.vayasu)
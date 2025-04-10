# WHY DATA STRUCTURES MATTER

"""
= They organize, store and manage data in ways that make your program more efficient, readable, and powerful.
= Diffrent problems need diffrent way to store and retrieve data.
= Lists are a great way for ordered collection you change .
= Tuples are like lists but immutable, perfect for mixed data.
= Dictionaries gives you fast access to data using keys.
= Using the right data structures makes your code faster.
= Looking up at an item in a dictionary is much faster thab a searching list
"""
"""
= They organize, store and manage data in ways that make your program more efficient, readable, and powerful.
= Diffrent problems need diffrent way to store and retrieve data.
= Lists are a great way for ordered collection you change .
= Tuples are like lists but immutable, perfect for mixed data.
= Dictionaries gives you fast access to data using keys.
= Using the right data structures makes your code faster.
= Looking up at an item in a dictionary is much faster thab a searching list.
= A set is great when you want to remove duplicates.
= Well chosen data structures make code easier to understand
    e.g 
    instead of:-
            names = ["Tilak", "Ansh", "Esha"]
            ages = ["18", "18", "20"]
        We can do this:
            students = {"Tilak" : 18,"Ansh" : 18,"Esha" : 20}
"""

"""
= python data structures come with powerfull builts-in methods
=advance data structures like queues, stacks, graphs and trees can be built
 using lists, dictonaries or classes. Understanding basic data structure 
 prepare you for more complex ones
"""


#LISTS
"""
    lists are ordered collections that contain eletments of different data types
    Properties:
        * Ordered
        * Mutable
        * They allow duplicates
"""

name = ["Esha", "Tilak", "Saleh", "Vansh", "Ansh", "Natasha", "Ansh" ]
#INDEXING
print(name[0]) #Esha
#SLICING
print(name[1:2]) #'Tilak'
#ADDING
name.append("Janet") #["Esha", "Tilak", "Saleh", "Vansh", "Ansh", "Natasha", "Ansh", "Janet" ]
#INSERTING
name.insert(1, "Joseph") #["Esha", "Joseph", "Tilak", "Saleh", "Vansh", "Ansh", "Natasha", "Ansh", "Janet" ]
#REMOVING
name.remove(0) #["Joseph", "Tilak", "Saleh", "Vansh", "Ansh", "Natasha", "Ansh", "Janet" ]
#POP
last_item = name.pop() #Janet
#LOOPING
for name in name:
    print(name) #Joseph, Tilak, Saleh, Vansh, Ansh,
#LENGTH
print(len(name)) #7
#LIST METHODS
name.sort() #sorts inn ascending order
name.reverse() #reverses the list


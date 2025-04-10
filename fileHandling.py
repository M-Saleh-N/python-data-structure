# FILE HANDLING AND STRING MANIPULATION 
"""
= File handling is essential for reading from and writing to files, as well as
 manipulating strings effectively
"""
# FILE HANDLING
"""
= Working with external data (txt, csv, json)
"""
#OPENING AND READING FILES 
# OPENING FILES
file = open("eample@.txt")
content = file.read()
print(content)
file.close()
# USING WITH
with open("example.txt", "r") as file :
    content = file.read()
    print(content)
# READING LINE BY LINE
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  
# WRITING TO FILES
with open("example.txt", "w") as file:
    file.write("Hello Rift Pro Software Engineering")
# APPEND TO A FILE
with open("output.txt", "a") as file:
    file.write("This is a new line Rift Pro Software Engineering\n")
#FILE MODES
"""
    "r" = Read (Default)
    "w" = Write (Overwrite)
    "a" = Append
    "r+" = Read and Write

"""

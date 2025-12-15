# f = open("scratch.txt" , "r")

# print(f.read())
# print(f.read(21)) #Reads the 21 characters
# print(f.readline()) #prints line 1 and a line break as well
# print(f.readline()) #prints line 2

# Using loop to run the file line by line
# with open("scratch.txt","r") as d:
#     for x in d:
#         print(x)


# Now we use the append or write method --- This will append in the next new line given
# with open("scratch.txt","a") as f:
#     f.write("Meow meow nigga")
#
# with open("scratch.txt",'r') as f:
#     print(f.read())

# To overwrite the whole text document
# with open("scratch.txt","w") as f:
#     f.write("Woops I deleted everything ")
# with open("scratch.txt","r") as f:
#     print(f.read())

# To create a new file
# f = open("demo.txt","x")

# To delete a file we need to import os then use this
# import os
# os.remove("demo.txt")

# To check if the file exist then remove it
# import os
# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
#     print("Demo file removed")
# else:
#     print("Demo file not found.")

# To delete an entire directory
import os
os.rmdir("meow meow nigga") # We can only remove Empty folders not folders with file in it

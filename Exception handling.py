# The Try block is used to check if a code block has some error in it
# And the Except Block is used to handle the error
# We can also use else which will let us handle all the execution when there is no error
# finally block executes all the code doesn't matter what try and except block have error or anything

# x = 1
# try:
#     print(x) #here x is not defined so it will give a error
# except:
#     print("No value is given to X") # now we declare the variable then it will print x


# We can also describe as many exceptions as we want theres no limit
# try:
#     print(x)
# except NameError:
#     print("No value found")
# except:
#     print("Something went wrong")

# now to use try block with else
# try:
#     print("Hello World")
# except:
#     print("Oops")
# else:
#     print("Nothing went wrong so code runs smoothly") # this code will print both try and else block as there is no error in the try block

# The finally block code will execute everytime even if there is an error
# try:
#     print(x)
# except:
#     print("Oops! Variable is undefined")
# finally:
#     print("I don't give a shit")

# We open a file and write something in it
# try:
#     f =  open("demo.txt")
#     try:
#         f.write("Hello World")
#     except:
#         print("Error! Something went wrong while writing file.")
#     finally:
#         f.close()
#         print("file closed") # Always executed
# except:
#     print("Error! Something went wrong. while opening file.") # The output will include this line and the finally block because there is no file named as demo.txt

# We can also choose to raise an exception and also handle the errors using except block
# x = -1
# try:
#     if x<0:
#         raise ValueError
# except ValueError:
#     print("Please enter a non-negative integer")

# we can always defined what type of error we want to define, we can choose any type of error we want
# x = "2"
# try:
#     if not type(x)==int:
#         raise ZeroDivisionError
#     else:
#         print("There is no error")
# except ZeroDivisionError:
#     print("Error")




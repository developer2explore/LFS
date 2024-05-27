# variable declasration
x = 5
y = "John"
print(x)
print(y)

# multiple variable declaration
a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)


# define a variable as local
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# define a variable as global
y = "old variable"

def myglobalfunc():
    global y
    print("declared variable is " + y)
    y = "new variable"

myglobalfunc()
print("declared variable is " + y)

#data types
intVariable = 5
print("declared variable type is " + type(intVariable))

floatvariable = 5.5
print("declared variable type is " + type(floatvariable))

stringvariable = "purushoth"
print("declared variable type is " + type(stringvariable))

arrayvariable = ["1","2"]
print("declared variable type is " + type(arrayvariable))

tuplevariable = ("1","2")
print("declared variable type is " + type(tuplevariable))

dictvariable = {"name" : "John", "age" : 36}
print("declared variable type is " + type(dictvariable))








# Get user input for name and color
name = input("Enter your name: ")
color = input("Enter your favorite color: ")

# Print the combined sentence with proper formatting
print(name + " likes " + color)

              
# CTRL + / for commenting the selected lines
# # Get user input for name and color
# name = input("Enter your name: ")
# color = input("Enter your favorite color: ")

# # Print the combined sentence with proper formatting
# print(name + " likes " + color)
              
              

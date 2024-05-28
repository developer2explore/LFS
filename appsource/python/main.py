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
print("declared variable type is " + str(type(intVariable)))

floatvariable = 5.5
print("declared variable type is " + str(type(floatvariable)))

stringvariable = "purushoth"
print("declared variable type is " + str(type(stringvariable)))

arrayvariable = ["1","2"]
print("declared variable type is " + str(type(arrayvariable)))

tuplevariable = ("1","2")
print("declared variable type is " + str(type(tuplevariable)))

dictvariable = {"name" : "John", "age" : 36}
print("declared variable type is " + str(type(dictvariable)))

#type casting
e3x = 35e3
e3xy = 12E4
e3xyz = -87.7e100
e3xyza = True

print(e3x)
print(type(e3x))

print(e3xy)
print(int(e3xy))
print(type(e3xy))
print(type(int(e3xy)))

print(e3xyz)
print(type(e3xyz))

print(e3xyza)
print(type(e3xyza))

print(str(e3xyza))
print(type(str(e3xyza)))




# # Get user input for name and color
# name = input("Enter your name: ")
# color = input("Enter your favorite color: ")

# Print the combined sentence with proper formatting
print(name + " likes " + color)

              
# CTRL + / for commenting the selected lines
# # Get user input for name and color
# name = input("Enter your name: ")
# color = input("Enter your favorite color: ")

# # Print the combined sentence with proper formatting
# print(name + " likes " + color)
              
              

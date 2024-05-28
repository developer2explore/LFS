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

# # Print the combined sentence with proper formatting
# print(name + " likes " + color)

              
# CTRL + / for commenting the selected lines
# # Get user input for name and color
# name = input("Enter your name: ")
# color = input("Enter your favorite color: ")

# # Print the combined sentence with proper formatting
# print(name + " likes " + color)
              
#StringSlicing  
print("****************string***************")
         
stringSlicing = "Hello, World5. Hello, World!."
print(stringSlicing[2:5])

print(stringSlicing)
print(type(stringSlicing))
print(stringSlicing.upper())
print(stringSlicing.lower())
print(stringSlicing.capitalize())
print(stringSlicing.title())

print(stringSlicing.count("h"))
print(stringSlicing.count("o"))

print(stringSlicing.endswith("!."))
print(stringSlicing.find("o"))
print(stringSlicing.find("o", 5))
print(stringSlicing.replace("o", '0'))
astringSlicing = "Hello, World!"

print("Is Upper : ", astringSlicing.isupper())
print("Is Lower : ", astringSlicing.islower())
print("Is Alpha Numeric : ", astringSlicing.isalnum())
print("Is Alpha : ", astringSlicing.isalpha())

sastringSlicing = "he\nis\ngood"
print(sastringSlicing)
print(sastringSlicing.splitlines())
print(sastringSlicing.splitlines(True))

sastringSlicing = "Tutor Joes Computer Education"
print(sastringSlicing.split(" "))

sastringSlicing = "Tutor,Joes,Computer,Education"
print(sastringSlicing.split(","))

sastringSlicing="    Joes     "
print(len(sastringSlicing))
print(len(sastringSlicing.strip()))
print(len(sastringSlicing.lstrip()))
print(len(sastringSlicing.rstrip()))

ssastringSlicing='12-03-2020'
print(ssastringSlicing.partition('-'))

#f String
age = 36
txt = f"My name is John, I am {age}"
print(txt)
print("************arthimetic Operators*******")
#arthimetic Operators
a = 123
b = 10
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(2**3)

print("************assignment Operators*******")
#assignment Operators
a = 20
print(a)
a += 5  # a=a+5
print(a)
a -= 10  # a=a-10
print(a)
a *= 10  # a=a*10
print(a)
a /= 10
print(a)
a %= 10
print(a)
a **=10
print(a)
a //= 10 
print(a)

print("************comparison Operators*******")
#comparison Operators
a = 20
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


print("************logical Operators*******")
#logical Operators
a = 25
print(a >= 10 and a <= 20)
print(a >= 10 or a <= 20)
print(not(a >= 10 or a <= 20))
# returns False because not is used to reverse the result

print("************IF Statement in Python*******")
#IF Statement in Python
n = int(input("Enter The Number : "))
if n % 2 == 0:
    print(n, " is Even Number")
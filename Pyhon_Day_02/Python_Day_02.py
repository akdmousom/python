# Working with variable



'''
Variables

Variables are containers for storing data values.

Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

'''

x = 'hello world' # x will be "Hello world"
y = 24 # y will be 24
z = True # z will be true

print(x, y, z)

'''
Casting
If you want to specify the data type of a variable, this can be done with casting.

'''

x = int(3) # x will be 3
y = float(3.5) # y will be 3.5
z = str(3) # z will be '3'

print(x, y, z)


'''
Get the Type
You can get the data type of a variable with the type() function.

'''

x = 5 # x will be <class 'int'>
y = 'john' # x will be <class 'str'>
z = True # x will be <class 'bool'>

print(type(x), type(y), type(z))


'''
Case-Sensitive
Variable names are case-sensitive.

'''

a = 'AKD'
A = "Arijit Kumar Das" #A will not overwrite a

print(a, A)


'''
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

'''

# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:

'''
2myvar = "John"
my-var = "John"
my var = "John"

'''

# Remember that variable names are case-sensitive


'''
Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

Camel Case
Each word, except the first, starts with a capital letter:

myVariableName = "John"

Pascal Case
Each word starts with a capital letter:

MyVariableName = "John"

Snake Case
Each word is separated by an underscore character:

my_variable_name = "John"

'''


# Many Values to Multiple Variables

# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"

print(x, y, z)

'''
One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:

'''

x = y = z = "Orange"

print(x,y,z)


'''
Unpack a Collection

If you have a collection of values in a list, tuple etc. 
Python allows you to extract the values into variables. This is called unpacking.

'''

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x,y,z)


'''
Global Variables

Variables that are created outside of a function 

(as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

'''




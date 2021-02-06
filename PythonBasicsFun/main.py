import hello_world
import math
import random
# to use deep copy
import copy

#data types
# int, float, double, str, list, tuple, dict, set, etc.
x = 10
# print(x, type(x))
x = "hello"
# print(x, type(x))

# operators
# /floating point div
# / / int divison
# ** exponentiation
# can also use math.pow() and other functions...
# print(math.pow(2, 5))

# user input
"""
fave_num = int(input("Enter your favorite number: "))
print(fave_num, type(fave_num))
"""

# conditionals
"""
temperature = 37
if temperature > 32:
    print("It's hot out")
else:
    print("It's cold outside")
"""
# use 'elif' for else if

# loops
# while and for loops
# for (int i = 0; i < 5; i++) { } doesn't exist
"""
for i in range(5):
    print(i, end = " ")
"""

# In-class Warm-Up Task

# Write a for loop to print the first 20 even numbers all on one line separated by a comma and a space
"""
for (i) in range(21):
    if i % 2 == 0:
        print(i, end = " ")
"""

# FUNCTIONS
"""
def print_even_numbers(stop=40):
    for (i) in range(2, 42, 2):
        print(i, end = ", ")

print_even_numbers(20)
"""

# RANDOM NUMBERS (import random)
random.seed(0)
die_roll = random.randint(1,6)
# print(die_roll)

# DECIMAL FORMATTING (ROUNDING)
# print(math.pi, round(math.pi, 2))

# C Style
# print("%.2f" %(math.pi))

# Pythonic
# print("{:.2f}".format(math.pi))

# lists
# like arrays, but can grow/shrink in size
# lists are objects, they have methods
# <object>.<method>()
# can have mixed types
fibs = [1, 1, 2, 3, 5, 8]
# print(fibs)
"""
for value in fibs:
    print(value, end=", ")
"""

# use len() to get the number of items in the list
"""
for i in range(len(fibs)):
    print(i, ":", fibs[i])
"""

# Built in Functions
"""
print("Sum = ", sum(fibs))
print("Max = ", max(fibs))
print("Min = ", min(fibs))
"""

# list methods
fibs.append(13)
# print(fibs)

fibs.pop()
# print(fibs)

# Nested lists
# we will use a nested list to store tabular data
matrix = [[0, 1, 2], [3, 4, 5]]

# Task: define/call pretty_print(table)
# prints the nested list in a nice grid structure
"""
def pretty_print(table):
    for line in table:
        print(line)
        for item in line:
            print(item, end = " ")
        print("")

pretty_print(matrix)
"""

# Python is pass by OBJECT REFERENCE
# object references are passed by value

def add_one(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] += 1
"""
print(matrix)
add_one(matrix)
print(matrix)

def clear_out(table):
    table = []

clear_out(matrix)

print(matrix)
"""

# shallow vs deep copy
# matrix_copy = matrix.copy() # makes a shallow copy
# shallow copy: copies the references to objects, not the objects themselves
# matrix_deep_copy = copy.deepcopy(matrix)
# deep copy: copies the objects themselves
"""
print("Matrix before:", matrix)
print("Matrix copy before:", matrix_copy)
print("Matrix deep copy before:", matrix_deep_copy)

add_one(matrix)
print("Adding one ...")
print("Give me a sec...")

print("Matrix before:", matrix)
print("Matrix copy before:", matrix_copy)
print("Matrix deep copy before:", matrix_deep_copy)
"""
# moral of the story - you want a deep copy to be safe
# using .copy() will likely bring about bugs

# file IO
# we want to load the contents of a csv file

def convert_to_numeric(values):
    # try to convert each value in values to a numeric type
    # skip over values that can't be converted (ie; titles)
    for i in range (len(values)):
        try:
            numeric_value = int(values[i])
            # successfully stored value at values[i]
            values[i] = numeric_value # put it back as an int
        except ValueError:
            print(values[i], " cannot be converted to an int")


def read_table(filename):
    table = []
    # 1. Open the file
    infile = open(filename, "r")

    # 2. Processing (reading/writing) each line as string element in an array
    lines = infile.readlines()

    for line in lines:
        line = line.strip() # Remove leading and trailing whitespace characters
        values = line.split(",") # Split the string by comma into a list of strings
        table.append(values)
        print(values)

    # print(lines)

    #3. Close
    infile.close()

    return table

table = read_table("msrp.csv")
# print(table)
# course = "python programming"
# print(len(course))

# print(course[:0])
# print(course[-1])

# print(course[0:3])
# print(course[:3])

# print(course[:])
# print(course[0:])
# \\\\\\\\\\\\\\\\\\\\\\\\\\

# course = "python \"programming"
# print(course)
# course = 'python " programming'
# print(course)

# course = "python \\ programming"
# print(course)
# course = "python \nprogramming"
# print(course)


# first = "masa"
# last = "jamal"
# full = first+" "+last
# print(full)


# first = "masssa"
# last = "jamal"
# full = f"{len(first)} {2+2}"
# print(full)


# course = " python programming"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.lstrip())
# print(course.find("pro"))
# print(course.replace("p", "j"))
# print("pro" in course)
# print("swift" not in course)


# print(10+3)
# print(10-3)
# print(10*3)
# print(10/3)
# print(10//3)
# print(10 % 3)
# print(10**3)


# x = 10
# x = x+3
# x += 3


# import math

# print(round(2.9))
# print(abs(-2.9))

# print(math.ceil(2.2))
# print(math.floor(2.2))


# x = input("x: ")
# y = int(x)+1
# print(f"x: {x},y: {y}")


# "1" + 1

# int(x)
# float(x)
# bool(x)
# str(x)


# Falsy "" 0 None


# print(bool(-1))

# print(ord("b"))
# print(ord("B"))

# print("zebra" > "apple")


# mark = 85

# if mark >= 90:
#     print("vgood")
# elif mark >= 80:
#     print("good")
# elif mark >= 70:
#     print("ok")
# else:
#     print("bad")
# print("done")


# and or not


# for number in range(1, 9, 3):
#     print("masa", number+1, (number+1)*".")


# for x in range(4):
#     for y in range(2):
#         print(f"({x},{y})")


# print(type(range(9)))


# iterable
# for x in "Python":
#     print(x)

# for x in [1, 2, 3, 4]:
#     print(x)


# num = 100
# while num > 0:
#     print(num)
#     num = num//2  # num//=2


# command = ""
# while command != "quite" and command !=" QUITE":
#     command = input(">")
#     print("ECHO", command)


# command = ""
# while command.upper() != "QUIT":
#     command = input(">")
#     print("ECHO", command)


# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() != "quit":
#         break


# make your own function
# def greet():
#     print("hi")
#     print("welcome")

# greet()


# def greet(f_name, l_name):
#     print(f"hi {f_name} {l_name}")
#     print("welcome")


# greet("masa", "jamal")
# greet("misk", "hayat")


# we have 2 type of function :
# 1- perform a task
# 2- return a value

# def greet(name):
#     print(f"Hi{name}")
# def get_greeting (name):
#     return f"Hi {name}"
# msg= get_greeting("misk")
# file=open("content.txt","w")
# file.write(msg)


# Keyword Arguments
# def increment(num, by):
#     return num+by

# print(increment(2, by=1))

# 1
# def multiply(*num):
#     print(num)

# multiply(2, 3, 4, 5)

# 2
# def multiply(*num):
#     for number in num:
#         print(number)


# multiply(6, 8, 7, 9, 8)

# 3
# def multiply(*num):
#     total=1
#     for number in num:
#         total*= number
#     return total


# print(multiply(6, 8, 7, 9, 8))


# def myfunc():
#     global x #global variable inside a function

# x = "masa"

# myfunc()

# print("my name is "+x)


# Data Type
# x=5 int
# x="hi" str
# x=2.5 float
# x=1j complex
# x=[1,2] list
# x={1,2}  set
# x={"one":1,"two":2}  dict
# x=(1,2) tuple
# x={"one","two"} set
# x=frozenset({"one","two"}) frozenset
# x=True bool
# x=b"hi" byte
# x=bytearray(9) bytearray
# x=memoryview(byte(9)) memoryview
# x=None nonetype


# import random
# print(random.randrange(1, 10)) #wiithout 10
# random.randint(1, 10) #with 10


# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)


# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"


# a = "Hello, World!"
# print(a.replace("l", "y"))


# #result always list
# numbers = "10-20-30-40"
# print(numbers.split("-"))


# name = "Masa Jamal Abulawi"
# print(name.split(" "))


# a = "Hello, World!"
# print(a.split(","))


# email = "masa@gmail.com"
# print(email.split("@"))


# String Concatenation
# a = "Hello"
# b = " World"
# c = a + b
# print(c)
# //////////////////////////////////////


# #loop with list
# thislist = ["a", "b", "c"]
# for i in range(len(thislist)):
#     print(thislist[i])


# # while loop with list
# thislist = ["a", "b", "c"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1


# # short syntax
# thislist = ["a", "b", "c"]
# [print(x) for x in thislist]


# # newlist = [expression for item in iterable if condition]

# firstList = ["m", "a", "s", "y", "a"]
# secList = [x for x in firstList if x != "a"]
# fruits = ["apple", "banana", "mango"]
# newlist = [x for x in fruits]
# newlist = [x for x in range(10)]
# newlist = [x for x in range(10) if x < 5]
# newlist = ["hello" for x in fruits]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# newlist = [x.upper() for x in fruits]
# print(newlist)
# print(secList)


# # Sort Descending
# thislist = ["o", "ma", "mz", "M", "b", "a"]
# thislist.sort(reverse=True)#Descending
# print(thislist)
# thislist.sort() # ascending, by default:
# print(thislist)

# Reverse Order

# thislist = ["b", "O", "K", "c"]
# thislist.reverse()
# print(thislist)


# # Copy a List
# flist = ["a", "b", "c"]
# slist = flist.copy()
# thlist = list(flist)
# folist = flist[:]
# print(flist, slist, thlist, folist)


# # Join Two Lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# firstWay
# list1.extend(list2)
# print(list1)
# another way
# list3 = list1 + list2
# print(list3)
# way3 :for x in list2:
# for x in list2:
#     list1.append(x)
# print(list1)


# //////////////////////
# # tuple
# thistuple = ("apple",)
# print(type(thistuple))

# # NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))


# Change Tuple Values or add item or remove
# Convert the tuple into a list to be able to change it:
# x = ("a", "b", "c")
# y = list(x)

# y[1] = "yy" (change)

# y.append("yyy")  (add)

# y.remove("a") (remove)

# x = tuple(y)
# print(x)


# delete the tuple completely:
# x = ("a", "b", "c")
# del x


# # add tuple to tuple
# x = ("a", "b", "c")
# y = ("1",)
# x += y
# print(x)


# # Unpacking a tuple:
# x = ("a", "b", "c")
# (mm, aa, ss) = x
# (yy, *masa) = x If # variables < number of values
# print(mm)
# print(aa)
# print(ss)
# print(yy)
# print(masa)


# # Loop Through a Tuple
# thistuple = ("a", "b", "c")
# for x in thistuple:
#     print(x)
# # or with index num
# for i in range(len(thistuple)):
#     print(thistuple[i])
# # or using while loop
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i = i + 1


# # Join Two Tuples
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)
# # Multiply Tuples
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)


# ////////////////////////////////////////

# Python Sets
# True and 1 :same value in sets
# False and 0:same value in sets
# 1.Once a set is created, you cannot change its items,
# but you can remove items and add new items.
# 2.Sets cannot have two items with the same value.
# 3.cannot be referred to by index or key.
# 4.A set can contain different data types:
# set1 = {"abc", 34, True, 40, "male"}
# 5.You cannot access items in a set by referring to an index or a key.


# 6.Loop through the set, and print the values:
# thisset = {"a", "b", "c"}
# for x in thisset:
#   print(x)

# 6.or ask if a specified value is present in a set
# thisset = {"a", "b", "c"}
# print("b" in thisset)
# print("c" not in thisset)

# 7.Add Items
# thisset.add("e")

# 8.use the update() method ,
# it can be any iterable object (tuples, lists, dictionaries etc.).
# thisset = {"a", "b", "c"}
# new={"l","2"} #set
# new=["5","7"] #list
# thisset.update(new)


# 9.To remove an item : remove(), or the discard()
# thisset.remove("b")
# thisset.discard("b")

# 10.Remove a random item by using the pop() method:
# x = thisset.pop()
# print(x)

# 11.The clear() method empties the set:
# thisset.clear()

# 12.The del keyword will delete the set completely:
# del thisset


# 13. join set
#  1.(union()  or  | operator )and update() : joins all items from both sets.
# set3 = set1.union(set2)
# set3 = set1 | set2
# myset = set1.union(set2, set3, set4)

#  2.Join a Set and a Tuple
# z = x.union(y)
#  3.
# set1.update(set2) / changes the original set


# //Note: Both union() and update() will exclude any duplicate items.//


#  4.: Keep ONLY the duplicates
# set3 = set1.intersection(set2) //any type
# or this way &
# set3 = set1 & set2 // set with set

#  5.:Keep all items from set1 that are not in set2:
# set3 = set1.difference(set2) //any type
# or this - //set with set


#  6.  keep the items from the first set that are not in the other set,
# set1.difference_update(set2)

#  7. keep only the elements that are NOT present in both sets.
# set3 = set1.symmetric_difference(set2)
# same as ^
# set3 = set1 ^ set2

#  8. keep all
# set1.symmetric_difference_update(set2)


# 14.frozenset is an immutable version of a set.
# x = frozenset({"a", "b", "c"})
# print(x)


# ///////////////////////

# Python Dictionaries
#  do not allow duplicates
# thisdict = {
#     "one": "1",
#     "two": "2",
#     "three": 3
# }
# x = thisdict["one"]
# print(x)
# x = thisdict.get("two")
# print(x)
# x = thisdict.keys()
# print(x)
# thisdict["four"] = "4"
# print(x)
# x = thisdict.values()
# print(x)
# x = thisdict.items()
# print(x)
# if "three" in thisdict:
#     print("Yes")
# thisdict["four"] = "8"
# print(x)
# thisdict.update({"four": 6})
# x = thisdict.items()
# print(x)
# thisdict.pop("one")
# print(thisdict)
# thisdict.popitem() # pop removes the last inserted item
# print(thisdict)
# del thisdict["two"]
# print(thisdict)
# del thisdict # delete the dictionary completely

# # to copy dict
# mydict = thisdict.copy()
# print(mydict)
# # another way
# mydict = dict(thisdict)
# print(mydict)


# //////////////////////
# if elif else

# age = 20
# if age < 13:
#   print("Child")
# elif age < 18:
#   print("Teenager")
# else:
#   print("Adult")


# pass :The pass statement is a null operation

# score = 85
# if score > 90:
#   pass


# Match Statement


# day = 4
# match day:
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")
#   case _: #The value _ will always match
#     print("Weekend")

# -----------
# month = 5
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5: #character | as an or operator
#     print("weekday")
#   case 6 | 7 if month == 5: #You can add if statements
#     print("weekends!")


# ////////////////////
# While Loops , break , continue , else
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break # or  continue , else
#   i += 1


# //////////////////////
# # For Loops
# # 1.Looping Through a String
# for x in "banana":
#   print(x)

# ////  break  and continue
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break # or continue
#   print(x)


# ///////  range()
# for x in range(6):
#   print(x)
# for x in range(2, 6):
#   print(x)
# for x in range(2, 30, 3):
#   print(x)


# /////Else in For Loop

# for x in range(6):
#     if x == 3:
#         break
#     print(x)
# else:
#     print("Finally finished!")


# #   ////// Nested Loops
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)


# /////pass
# for x in [0, 1, 2]:
#   pass


# ////////////////////////////////////
# # Function
# # parameter and argument
# def my_function(name): # name is a parameter
#   print("Hello", name)

# my_function("Emil") # "Emil" is an argument


# //////
# Sending a (list )as an argument:

# def my_function(fruits):
#     for fruit in fruits:
#         print(fruit)


# my_fruits = ["apple", "banana", "cherry"]
# my_function(my_fruits)


# # Sending a (dictionary) as an argument:
# def my_function(person):
#     print("Name:", person["name"])
#     print("Age:", person["age"])


# my_person = {"name": "mas", "age": 25}
# my_function(my_person)


# ///////////////////
# Positional-Only Arguments
# With , /, you will get an error if you try to use keyword arguments:

# def my_function(name, /):
#   print("Hello", name)

# my_function(name = "Emil") #with ,/ & without name


# /////// Keyword-Only Arguments

# def person(*, name, age):
#     print(name, age)
# person(name="Masa", age=17) # specify that a function
# person("Masa", 17) # error


# /////Arguments before / are positional-only, and arguments after * are keyword-only


# /////////////////
# 1. *args Accept many positional arguments
# Becomes a tuple

# def add(*numbers):
#     print(numbers)   # tuple
# add(1, 2, 3)


# # 1.2 Unpacking a list with *
# def add(a, b, c):
#     print(a + b + c)

# numbers = [1, 2, 3]

# add(*numbers)


# \\\\\
# 2. **kwargs Accept many keyword arguments
# Becomes a dictionary

# def person(**data):
#     print(data)
# person(name="Masa", age=17)


# # 2.2 Unpacking a dictionary with **
# def hello(fname, lname):
#     print(fname, lname)

# person = {
#     "fname": "Masa",
#     "lname": "Abulawi"
# }

# hello(**person)

# /////////////////////////


# # nonlocal -> modify outer function variable

# # global -> modify global variable
# x = "Global"


# def outer():
#     x = "Enclosing"

#     def inner():
#         nonlocal x
#         x = "Changed by inner"

#         y = "Local"
#         print("Inside inner:")
#         print("x =", x)
#         print("y =", y)

#     inner()

#     print("\nInside outer:")
#     print("x =", x)


# outer()

# print("\nOutside functions:")
# print("x =", x)


# \\\\\\\\\\\\\\\
# Decorator
# def welcome(func):

#     def wrapper():
#         print("Welcome!")
#         func()
#     return wrapper

# @welcome  #Decorator
# def masa():
#     print("I am Masa")
# masa()


# //////////
# lambda arguments: expression , Can have many arguments
# Common with:
# map()
# filter()
# sorted()

# square = lambda x: x * x #== def square(x):  return x * x
# print(square(4))


# # //////////// recursive 1: Countdown 2: Factorial 3: Fibonacci 4: Sum of List 5: Find Maximum in List
# print(factorial(5))
# def factorial(n):
#     # Base case: stop at 0 or 1
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)  # recursive step
# print(factorial(5))

# ///////////
# # Generator( next , send , close)
# def simple():
#     name = yield "Enter your name:"
#     print("Hello", name)

# gen = simple()
# print(next(gen))
# gen.send("masa")
# gen.close()


# ////////////////////////////////
# # Python Lists
# cars = ["Ford", "Volvo", "BMW"]
# cars.append("Honda")     # add
# cars[1] = "Toyota"       # edit
# cars.pop(0)              # remove

# for car in cars:
#     print(car)

# print(len(cars))


# ///////////////////////////////////
# # Python Iterators
# #  tuple or  Lists, dictionaries, and sets are all iterable objects.
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# # Print the first item
# print(next(myit))


# ////////////////////////////////////
# 1.module (create new file then import here)
# import mymodule
# mymodule.greeting("Masa")


# # 2.Re-naming a Module
# import mymodule as mx

# print(mx.name)
# print(mx.age)
# mx.greeting("Masa")


# # 3.Import From Module
# from mymodule import greeting
# greeting("Masa")


# # 4. printing all variables (dir)
# import mymodule
# print(dir(mymodule))


# ////////////////////////////////////
# # Python Datetime
# import datetime
# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%A")) # Full weekday name
# # Create a specific date
# date = datetime.datetime(2026, 6, 25)


# /////////////////////////////////////
#  Python JSON
# JavaScript Object Notation

# # 1.json to python  = json.loads()
# import json
# # JSON string
# data = '{ "name":"Masa", "age":22 }'
# person = json.loads(data)
# print(person["name"])
# print(person["age"])
# print(person)

# # 2.Python to JSON  = json.dumps()
# # Python dictionary
# person = {
#     "name": "Masa",
#     "age": 22
# }
# result = json.dumps(person)
# print(result)


# # 3.
# import json
# p = {"name": "masa jamal", "age": 22} #Format the Result ,indentations and line breaks.
# print(json.dumps(p, indent=5,  sort_keys=True)) #Order the Result


# /////////////////////////////////////////////
# Python RegEx
# import re
# words = "i want to travel to the spain"
# toSearch = re.search("^i.*spain$", words)

# if toSearch:
#     print("yes")
#     print(words)
# else:
#     print("no match")


# //////////////////////////////////////
# Python PIP
# import camelcase
# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt))


# //////////////////////////////////////////

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
# finally:
#     print("Program finished")


# ///////////////////////////////////////////
# Placeholders and Modifiers
# price = 20
# txt = f"The price is {price} dollars"
# print(txt)
# txt = f"The price is {price:.2f} dollars"
# print(txt)
# txt = f"The price is {50:.3f} dollars"
# print(txt)
# txt = f"The price is {2 * 30} dollars"
# print(txt)
# tax = 0.25
# txt = f"The price is {price + (price * tax)} dollars"
# print(txt)
# price = 49
# txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
# print(txt)
# fruit = "nablus"
# txt = f"I love {fruit.upper()}"
# print(txt)
# /////////////
# String format()
# price = 20
# txt = "The price is {} dollars"
# print(txt.format(price))
# # //
# price = 49
# txt = "The price is {:.2f} dollars"
# print(txt.format(price))
# # //
# age =10
# name = "misk"
# txt = "His name is {1}. {1} is {0} years old."
# print(txt.format(age, name))
# # //
# myorder = "I have a {carname}, it is a {model}."
# print(myorder.format(carname="Ford", model="Mustang"))


# ///////////////////////////////////////
# None
# x = None
# if x is None:
#     print("x is none")

# //////////////////////////////////////////


# name = input("Enter your name:")
# print(f"Hello {name}")
# # ///

# x = input("Enter a number:")
# y = math.sqrt(float(x))
# print(f"The square root of {x} is {y}")


# //////////////////////////////////////////
# class & object
# class newClass:
#     x = 7
#     y = 8
# p1 = newClass
# p2 = newClass
# p3 = newClass
# p4=newClass() #object
# print(p1.x)
# print(p2.y)
# print(p3.x)
# del p1


# ///
# having an empty class
# class Person:
#   pass


# ///
# Create a class
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def greet(self):
#     print("Hello, my name is " + self.name)

# # Create an object
# p1 = Person("John", 36)

# # Call the greet method
# p1.greet()

# /////////////////////////////////////////

# Create the Car class
# class Car:
#     def __init__(self, brand):
#         self.brand = brand

#     def show(self):
#         print(self.brand)


# # Create an object
# c1 = Car("Ford")
# # Call the show method
# c1.show()


# ////
# # Create the Student class
# class Student:
#   def __init__(self, name, grade):
#     self.name = name
#     self.grade = grade
# #  object
# s1 = Student("Anna", "A")
# print(s1.grade)
# s1.grade = "B"
# print(s1.grade)


# //////
# # Class Methods
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# r1 = Rectangle(5, 3)
# print(r1.area())


# ////
# Inheritance

# # Create the Animal class
# class Animal:
#   def __init__(self, name):
#     self.name = name
#   def speak(self):
#     print(self.name)
# # Create the Dog class (inherits from Animal)
# class Dog(Animal):
#   pass
# # Create an object
# d1 = Dog("Rex")
# d1.speak()


# ///////
# Encapsulation
# class ScoreBoard :
#   def __init__(self , score ):
#      self.__score=score
#   def get_score(self):
#      return  self.__score
# # Create an object
# s1 = ScoreBoard(0)
# print(s1.get_score())


# ///////////////////////////////////////////////////
# Python File

#   Open a File
# f = open("demofile.txt")
# print(f.read())


#  Using the with statement

# with open("demofile.txt") as f:
#     print(f.read())


#  Close Files

# f = open("demofile.txt")
# print(f.readline())
# f.close()

#    Read Only Parts of the File
# with open("demofile.txt") as f:
#     print(f.read(9))

# Read Lines
# with open("demofile.txt") as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())


# By looping through the lines of the file:
# with open("demofile.txt") as f:
#     for x in f:
#         print(x)


# ///////////////////////////////////////////////////////////

# Write to an Existing File
# with open("demofile.txt", "a") as f:
#     f.write("Now the file has more content!")

# with open("demofile.txt") as f:
#     print(f.read())


# Overwrite Existing Content

# with open("demofile.txt", "w") as f:
#     f.write("Woops! I have deleted the content!")

# with open("demofile.txt") as f:
#     print(f.read())


# Create a New File (x  - a - w)
# f = open("myfile.txt", "x")


# Delete a File
# import os
# os.remove("myfile.txt")


# Check if File exist:
# import os
# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print("The file does not exist")


# Delete Folder
# import os
# os.rmdir("New folder")

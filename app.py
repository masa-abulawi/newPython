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
thisdict = {
    "one": "1",
    "two": "2",
    "three": 3
}
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

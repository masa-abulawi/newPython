# Python Lists and Arrays
# Creating Lists

# myList = []
# newList = [1, 2, 5, 9, 8]
# typList = [1, "hi", 2.5, None, True]
# x = [1, 2, 6, 4, 7]
# x.append(5)
# # Sort list ascending:
# x.sort()
# print(x)


# Create an algorithm to find the lowest value in a list:(for small data sets)
# x = [1, 5, 4, 3, 8, 2, 9]
# minVal = x[0]
# for i in x:
#     if i < minVal:
#         minVal = i
# print("the lowest value :", minVal)


# Stacks with Python / LIFO /  linear data structure /
# push: Adds /pop : Removes and returns the top
# Peek: Returns the top (last)
# isEmpty: Checks  / Size: Finds the number of elements


# Stack Implementation using Python Lists
# stackasList = []
# stackasList.append("a")
# stackasList.append("5")
# stackasList.append("b")
# stackasList.append("7")
# stackasList.append("c")
# print(stackasList)
# # //////pop
# stackasList.pop()
# print(stackasList)
# # /////peek
# print(stackasList[-1])
# # ///////////
# if (len(stackasList) == 0):
#     print("is empty")
# else:
#     print("is not empty")
# # /////////
# if not stackasList:
#     print("yes")
# else:
#     print("no")
# # ////////size
# print(len(stackasList))


# Stack Implementation using Linked Lists
# class Node :
#     def __init__(self,value):
#         self.value=value
#         self.next=None
# class Stack :
#     def __init__(self)    :
#         self.head=None
#         self.size=0


#     def push(self,value):
#         new_node =Node(value)
#         if self.head:
#             new_node.next=self.head
#             self.size+=1


#     def pop (self):
#         if self.isEmpty():
#            return "stack is empty"
#         popped_node = self.head
#         self.head=self.head.next
#         self.size -=1
#         return popped_node.value


#     def peek (self):
#         if self.isEmpty():
#            return "stack is empty"
#         return self.head.value


# ////////
# stack = []
# stack.append("ali")
# stack.append("sara")
# stack.append("omar")
# stack.append("lina")
# print(stack)
# stack.pop()
# print(stack)
# print(stack[-1])
# print(len(stack))
# if (len(stack) == 0):
#     print("is empty")
# else:
#     print("not empty")
# print(stack)

# if not stack:
#     print("its empty")
# else:
#     print("not empty")


# ///////////
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):

        if self.head is None:
            return "Stack is empty"

        popped = self.head
        self.head = self.head.next
        return popped.value

    def peek(self):
        if self.head is None:
            return "stack is empty"
        return self.head.value


s = stack()

s.push("A")
s.push("B")
s.push("C")

print(s.peek())

print(s.pop())
print(s.pop())
print(s.pop())

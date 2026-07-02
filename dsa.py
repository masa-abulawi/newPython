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


# ///////

# # Creating a stack using class:

# class Stack:
#   def __init__(self):
#     self.stack = []

#   def push(self, element):
#     self.stack.append(element)

#   def pop(self):
#     if self.isEmpty():
#       return "Stack is empty"
#     return self.stack.pop()

#   def peek(self):
#     if self.isEmpty():
#       return "Stack is empty"
#     return self.stack[-1]

#   def isEmpty(self):
#     return len(self.stack) == 0

#   def size(self):
#     return len(self.stack)


# //////

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
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class stack:
#     def __init__(self):
#         self.head = None

#     def push(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node

#     def pop(self):

#         if self.head is None:
#             return "Stack is empty"

#         popped = self.head
#         self.head = self.head.next
#         return popped.value

#     def peek(self):
#         if self.head is None:
#             return "stack is empty"
#         return self.head.value


# s = stack()

# s.push("A")
# s.push("B")
# s.push("C")

# print(s.peek())

# print(s.pop())
# print(s.pop())
# print(s.pop())


# # ////////////////////////////////////////////////////
# Queues with Python
#  that follows the First-In-First-Out (FIFO) principle.


# # Queue Implementation using Python Lists
# queue = []

# # Enqueue = add
# queue.append('A')
# queue.append('B')
# queue.append('C')
# queue.append("D")
# print(queue)

# # Peek (return first )(A)
# F = queue[0]
# print(F)

# # Dequeue = delete first = pop (A)-(B,C,D)
# P = queue.pop(0)
# print(P)
# print(queue)

# # isEmpty (false)
# isEmpty = not bool(queue)
# print(isEmpty)

# # size(3)
# print(len(queue))


# ////////////////
# # Implementing a Queue Class
# class Queue:
#     def __init__(self):
#         self.queue = []
#         # enqueue = add

#     def enqueue(self, element):
#         self.queue.append(element)
#         # dequeue = del first = pop

#     def dequeue(self):
#         return self.queue.pop(0)
#     # peek = return first

#     def peek(self):
#         return self.queue[0]
#     # isEmpty

#     def isEmpty(self):
#         return len(self.queue) == 0
#     # size

#     def size(self):
#         return len(self.queue)


# # Create a queue
# myQueue = Queue()

# myQueue.enqueue('A')
# myQueue.enqueue('B')
# myQueue.enqueue('C')

# print("Queue: ", myQueue.queue)
# print("Peek: ", myQueue.peek())
# print("Dequeue: ", myQueue.dequeue())
# print("Queue after Dequeue: ", myQueue.queue)
# print("isEmpty: ", myQueue.isEmpty())
# print("Size: ", myQueue.size())


# ////////////////////////////////////////////////

# # Queue Implementation using Linked Lists
# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Queue:

#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.length = 0

#     def enqueue(self, element):
#         new_node = Node(element)
#         if self.rear is None:  # (is empty?)
#             self.front = self.rear = new_node
#             self.length += 1
#             return
#         self.rear.next = new_node
#         self.rear = new_node
#         self.length += 1

#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty"

#         temp = self.front
#         self.front = temp.next
#         self.length -= 1

#         if self.front is None:
#             self.rear = None

#         return temp.data

#     def peek(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.front.data

#     def isEmpty(self):
#         return self.length == 0

#     def size(self):
#         return self.length

#     def printQueue(self):
#         temp = self.front
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print()


# # Create a queue
# myQueue = Queue()

# myQueue.enqueue('A')
# myQueue.enqueue('B')
# myQueue.enqueue('C')

# print("Queue: ", end="")
# myQueue.printQueue()
# print("Peek: ", myQueue.peek())
# print("Dequeue: ", myQueue.dequeue())
# print("Queue after Dequeue: ", end="")
# myQueue.printQueue()
# print("isEmpty: ", myQueue.isEmpty())
# print("Size: ", myQueue.size())


# //////////////////////////////////////////////////////
# class Node :
#     def __init__(self,data):
#         self.data=data
#         self.next=None

#     def traverseAndPrint(head):
#         currentNode = head
#         while currentNode:
#             print(currentNode.data, end=" -> ")
#             currentNode = currentNode.next
#         print("null")

#     def findLowestValue(head):
#         minValue = head.data
#         currentNode = head.next


#         while currentNode:
#             if currentNode.data < minValue:
#                 minValue =currentNode.data
#             currentNode= currentNode.next

#         return minValue


#     def deleteSpecificNode(head , nodeToDelete):
#         # delete the first value head
#         if head == nodeToDelete :
#             return head.next

#         # delete any value
#         currentNode = head

#         while currentNode.next and currentNode.next != nodeToDelete:
#             currentNode = currentNode.next
#         if currentNode.next is None:
#                 return head
#         currentNode.next = currentNode.next.next
#          return head


# ///////////////////////////////////////
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def traverseAndPrint(head):
#   currentNode = head
#   while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
#   print("null")

# def insertNodeAtPosition(head, newNode, position):
#   if position == 1:
#     newNode.next = head
#     return newNode

#   currentNode = head
#   for _ in range(position - 2):
#     if currentNode.next is None:
#       break
#     currentNode = currentNode.next

#   newNode.next = currentNode.next
#   currentNode.next = newNode
#   return head


# ///////////////////////////////////////
# # hash code
# my_list = [[] for _ in range(10)]


# def hash_function(value):
#     sum_of_char = 0
#     for char in value :
#         sum_of_char += ord(char)


#     return sum_of_char%10


# def add(name):
#     index =hash_function(name)
#     # without collision / chaining
#                 #  my_list[index] = name
#     # collision / chaining make a list for every bucket
#     my_list[index].append(name)


# def contains(name):
#         index =hash_function(name)
#         return my_list[index] == name


# def remove(name):
#     index = hash_function(name)

#     if name in my_list[index]:
#         my_list[index].remove(name)
#         return True

#     return False


def display():
    for index, bucket in enumerate(my_list):
        print(f"{index}: {bucket}")


# ////////////////////////////////////////////////

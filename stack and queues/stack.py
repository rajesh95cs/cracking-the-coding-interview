#generic class program which creates a stack object which does all the basic
#operations using a stack(push,pop,whether the stack is empty,the top element of the stack)
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def __str__(self):
         out = ""
         for item in reversed(self.items):
            out += str(item)
            out += "-->"
         return out

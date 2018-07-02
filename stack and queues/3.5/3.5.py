#program implemented to sort a set of unsorted data using stacks
#here we use 3 stacks to accomplish our task

#basic operation and features regarding the stack is imported from a file
import sys
sys.path.append("../")
from stack import *



def stack_sort(unsorted_data):
    stack1 = Stack()
    stack2 = Stack()
#here stack3 is used as an extra buffer to store min elements in ascending order
#ie the greatest elements will be at the top positions
    stack3 = Stack()
#loop through the input list to push the unsorted in to stack1
    for data in unsorted_data:
        stack1.push(data)
#initialy the before poping from stack1 the top element of stack1 is stored in
#in a temporary buffer
    min = stack1.peek()
    #print(stack1)
#in this block of statments the sorting happens
#outer while loop says that the sorting should happen till the size of the
#unsorted sequence
    while stack3.size() < len(unsorted_data):
#inner loop
        while not stack1.isEmpty():
            if stack1.isEmpty():
                continue

            if stack1.peek() < min:
                min = stack1.peek()
            stack2.push(stack1.peek())
            stack1.pop()
        stack3.push(min)
        #print(stack3)
        while not stack2.isEmpty():
            #print(stack2)
            if stack2.peek() != min:
                stack1.push(stack2.peek())
            stack2.pop()
        if not stack1.isEmpty():
            min = stack1.peek()

    return stack3

if __name__ == '__main__':

    d = "dhlkb62746gdsbsd;lksd;"
    print(stack_sort(d))

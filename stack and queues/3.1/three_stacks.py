import sys
sys.path.append("../")
from stack import *


def three_stacks(stack1,stack2,stack3):
    combine_stacks = []
    combine_stacks.append(stack1)
    combine_stacks.append(stack2)
    combine_stacks.append(stack3)
    return combine_stacks

if __name__ == '__main__':
    stack1 = Stack()
    stack2 = Stack()
    stack3 = Stack()
    stack1.push(4)
    stack2.push(5)
    stack3.push(6)
    stack1.push(3)
    stack2.push(4)
    stack3.push(2)
    stack1.push(4)
    stack2.push(3)
    stack3.push(5)
    stack1.push(3)
    stack2.push(6)
    stack3.push(8)
    print(three_stacks(stack1,stack2,stack3))

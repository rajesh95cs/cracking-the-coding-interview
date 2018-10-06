import sys
sys.path.append("../")
from stack import *

main_stack = Stack()
min = Stack()
def min_pushing(arr,main_stack,min):
    main_stack.push(arr[0])
    min.push(arr[0])
    del(arr[0])
    for i in arr:
        if i < main_stack.peek():
            min.push(i)
            mail_stack.push(i)
        main_stack.push(i)
    return min
def min_pop(main_stack,min):
    temp = main_stack.pop()
    if temp == min.peek():
        min.pop()
    else:
        min_temp = min.pop()
        return min_temp
arr = [2,4,1,3,5,2,8,6,0]
print(min_pushing(arr,main_stack,min))
print(min_pop(main_stack,min))

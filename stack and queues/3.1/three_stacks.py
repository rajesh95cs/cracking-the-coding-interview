stack_size = 10
stack_pointer = [-1,-1,-1]
buffer = stack_size*3*[0]
def three_stacks():

    for i in range(4):
        print "enter stack number"
        stack_num = int(raw_input())
        if stack_num < 3:
            for j in range(4):
                print "enter value"
                value = int(raw_input())
                push(stack_num,value)
        else:
            return "only 3 stacks allowed ie 0,1,2"
    print buffer
    for i in range(4):
        print "enter stack number "
        stack_num = int(raw_input())
        if stack_num < 3:
            print pop(stack_num)

        else:
            return "only 3 stacks allowed ie 0,1,2"
    print buffer
    print "enter stack number "
    stack_num = int(raw_input())
    print peek(stack_num)
    


def push(stack_num,value):
    if stack_pointer[stack_num]+1 >= stack_size:
        return "stack is full"
    else:
        stack_pointer[stack_num] += 1
        buffer[top_of_stack(stack_num)] = value
def pop(stack_num):
    if is_empty(stack_num):
        return "stack is empty"
    else:
        temp = buffer[top_of_stack(stack_num)]
        buffer[top_of_stack(stack_num)] = 0
        stack_pointer[stack_num]-=1
        return temp

def peek(stack_num):
    if is_empty(stack_num):
        return "stack is empty"
    return buffer[top_of_stack(stack_num)]


def top_of_stack(stack_num):
    return stack_size*stack_num + stack_pointer[stack_num]

def is_empty(stack_num):
    return stack_pointer[stack_num] == -1

three_stacks()

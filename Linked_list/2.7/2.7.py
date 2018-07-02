import sys
sys.path.append("../linked_list_class")
sys.path.append("../../stack and queues")
from singly_linked_list_class import *
from stack import *

def palindrome(link_list):
    head_list = link_list.head
    stack_buff = Stack()
    while head_list is not None:
        stack_buff.push(head_list.data)
        head_list = head_list.next
    head_list = link_list.head
    for i in range(stack_buff.size()/2):
        if head_list.data != stack_buff.pop():
            return False
        head_list = head_list.next
    return True



if __name__ == '__main__':
    link_list = SinglyLinkedList()
    d ="RARZAMKTFXRSVOXNNXOVSDRXFTKMAZRAR"
    for letter in d:
        link_list.insertNodeAtTail(letter)
    print(link_list.head.data)
    print "the current link list is"
    print link_list
    if palindrome(link_list):
        print "it is a palindrome"
    else :
        print "it is not a palindrome"

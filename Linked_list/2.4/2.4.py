#import the features from the file linked_list_class which contains insertion
#operation deletion operation and creating a new linked list and nodes
import sys
sys.path.append("../linked_list_class")
from singly_linked_list_class import *

#rearrange_list function which accepts a linked list and an element x as
#parameter the operation done here is that we have to rearrange the list in such
#a way that elements which are lesser than x should be arrange to the left of x
#in any order and greater elemets should be place to the right of x irrespective of there
#order
def rearrange_list(x,link_list):
#smaller_than_x linked list is created to store elements lesser than x
    smaller_than_x = SinglyLinkedList()
#greater_than_x linked list is created to store elements greater than x
    greater_than_x = SinglyLinkedList()
#this list is created to store the elements with the value equal to x
    equal_x = SinglyLinkedList()
    head = link_list.head
#iterating through the main linked list link_list to divide the linked list in
#such a way that elements lesser than x is stored in smaller_than_x
#and elements greater_than_x is stored in greater_than_x linked list
#when the element in the linked list link_list matches with x it is stored to
#the linked list equal_x this is done till the end of the main list(link_list)
    while head is not None:
        if head.data < x:
            smaller_than_x.insertNodeAtTail(head.data)
        else:
            if head.data > x:
                greater_than_x.insertNodeAtTail(head.data)
            else:
                equal_x.insertNodeAtTail(x)
        head = head.next
#after the lists are divided next we merge all these linked list ie smaller_than_x
#equal_x and greater_than_x this is done by, we travers through the equal_x to
#get the end next value and the head of the greater_than_x is replaced with the
#end end next value of equal_x, and after that the end(next) value of smaller_than_x
#is repalced with the head of the equal_x list hence the merging is done
    smaller_head = smaller_than_x.head
    equal_tail = equal_x.head
    while equal_tail.next is not None:
        equal_tail = equal_tail.next
    equal_tail.next = greater_than_x.head
    if smaller_than_x.head is None :
        return equal_x
    while smaller_head.next is not None:
        smaller_head = smaller_head.next
    smaller_head.next = equal_x.head
    return smaller_than_x

if __name__ == '__main__':
    link_list = SinglyLinkedList()
    d = "dhlkbjstcrwomaxma12342353465463mpz"
    for letter in d:import sys
        link_list.insertNodeAtTail(letter)
    print(link_list.head.data)
    print "the current link list is"
    print link_list
    print(rearrange_list("5",link_list))

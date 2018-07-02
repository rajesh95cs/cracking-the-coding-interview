import sys
sys.path.append("../linked_list_class")
from singly_linked_list_class import *


def rearrange_list(x,link_list):
#smaller_than_x linked list is created to store elements lesser than x
    smaller_than_x = []
#greater_than_x linked list is created to store elements greater than x
    greater_than_x = []
#this list is created to store the elements with the value equal to x
    equal_x = []
    head = link_list.head

    while head is not None:
        if head.data < x:
            smaller_than_x.append(head.data)
        else:
            if head.data > x:
                greater_than_x.append(head.data)
            else:
                equal_x.append(x)
        head = head.next
    smaller_than_x.sort()
    greater_than_x.sort()
    arranged_list = SinglyLinkedList()
    for element in smaller_than_x:
        arranged_list.insertNodeAtTail(element)
    for element in equal_x:
        arranged_list.insertNodeAtTail(element)
    for element in greater_than_x:
        arranged_list.insertNodeAtTail(element)
    return arranged_list


if __name__ == '__main__':
    link_list = SinglyLinkedList()
    d = "dhlkbjstcrmpz"
    for letter in d:
        link_list.insertNodeAtTail(letter)
    print(link_list.head.data)
    print "the current link list is"
    print link_list
    print "the sorted arranged list is"
    print(rearrange_list("j",link_list))

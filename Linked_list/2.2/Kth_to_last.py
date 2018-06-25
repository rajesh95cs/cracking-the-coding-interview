import sys
sys.path.append("../linked_list_class")
from singly_linked_list_class import *


def kFrom_last(k,link_list):
    head1 = link_list.head
    head2 = head1
    for i in range(k):
        head1 = head1.next
    while head1 is not None:
        head1 = head1.next
        head2 = head2.next
    return head2.data

if __name__ == '__main__':
    link_list = SinglyLinkedList()
    d = "dN9c0ODx1Lbi6i9hDlfPsFrqrOOqfYBSOSPyCyUaId1dge7uWRYEpXl8ZuwmZcyrSiSf"
    for letter in d:
        link_list.insertNodeAtTail(letter)
    print "the inputed link list is"
    print link_list
    k = 20
    print "the %dth to the last element is %s"%(k,kFrom_last(k,link_list))

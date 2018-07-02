import sys
sys.path.append("../linked_list_class")
from singly_linked_list_class import *


def linked_list_nos(link_list1,link_list2):
    head1 = link_list1.head
    head2 = link_list2.head
    ans_list = SinglyLinkedList()
    carr = 0
    ans = 0
    while head1 is not None or head2 is not None:
        ans = head1.data + head2.data
        place_ans = ans%10
        place_ans += carr
        ans_list.insertNodeAtTail(place_ans)
        carr = ans/10
        if head1.next is None:
            break
        else:
            head1 = head1.next
        if head2.next is None:
            break
        else:
            head2 = head2.next
    if head1 is None:
        ans = head2.data
    elif head2 is None:
        ans = head1.data
        print "condi 1"
    place_ans = ans%10
    place_ans += carr
    ans_list.insertNodeAtTail(place_ans)
    carr = ans/10

    if carr != 0:
        ans_list.insertNodeAtTail(carr)
    return ans_list
if __name__ == '__main__':
    link_list1 = SinglyLinkedList()
    link_list2 = SinglyLinkedList()
    link_list1.insertNodeAtTail(7)
    link_list1.insertNodeAtTail(1)
    link_list1.insertNodeAtTail(6)
    link_list2.insertNodeAtTail(5)
    link_list2.insertNodeAtTail(9)
    #link_list2.insertNodeAtTail(2)

    print "  number 1 : ", link_list1
    print "  number 2 : ", link_list2
    print "the sum is : ", linked_list_nos(link_list1,link_list2)

#module which is designed to do the basic linked list operations like inserting a node
#deleting from current and from the end
#the module "copy" is imported to perform deep copy and shallow copy
import copy
#class named SinglyLinkedListNode which is defined to create a node for the linked link_list
#node is called as the object of this class this node object contains the data
#and the next variable contains the link to the next node in the linked list
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
#class SinglyLinkedList which is defined to create the singly linked list
#this class contains the head variable which is used to reference the linked linked list
#the head variable contains the address of the of the first node in the linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None
#the below function defined is to create a representation fuction which is used
#to display the linked list at the time of inputing and displaying the output
    def __str__(self):
        out = ""
#here deepcopy() is used instead of shallow copy because in shallow copy only the
#reference to the variable is changed instead of copying the whole data but in
#case of deepcopy a new memory is allocated and the value is stored in it
#here deepcopy is used because ............
        head = copy.deepcopy(self.head)
        while head.next is not None:
            out += str(head.data)
            out += " --> "
            head = head.next
        out += str(head.data)
        return out
#this function is defined to insert the node at the end of the linked list
#with the only argument data is accepted there are three case inserting when
#1)there is no element in the list. 2) when there is only one element in the link_list
#3)inserting at the end of the list
    def insertNodeAtTail(self,data):
#inserttion at the begin if head pointer is none just assign the node to the head
        if self.head is None:
            node = SinglyLinkedListNode(data)
            self.head = node
#insertion at the end of the list this is done by traversing through the linked link_list
#with head till it finds the next as none then assign the node to the next variable
        else:
            head = self.head
            while head.next is not None:
                head = head.next
            head.next = SinglyLinkedListNode(data)
            head.next.next = None

#deleteCurrNode() is defined to delete the current node where the pointer is present
    def deleteCurrNode(self, pointer):
#pointer is passed as the argument to know the present postion in the linked list
        if self.head.next is None:
            self.head = None
            return
        pointer.data = pointer.next.data
        pointer.next = pointer.next.next
#deleteLastNode() is defined to delete the last node in the linked list
#here three case can arise 1) when the list is an empty list 2)when there is
#only one element in the linked list and finaly iterating throught the list to
#find the last element in the linked list
    def deleteLastNode(self):
        head = self.head
        if head is None:
            return
        if head.next is None :
            self.head = None
        while head.next.next is not None :
            head = head.next
        head.next = None


if __name__ == '__main__':
    link_list = SinglyLinkedList()
    d = "followup"
    for letter in d:
        link_list.insertNodeAtTail(letter)
    print "the current link list is"
    print link_list
    #link_list.deleteLastNode()
    print "the linked list after deleting the last node"
    print link_list
    link_list.deleteCurrNode(link_list.head)
    print "deleting the 2nd node"
    print link_list
    link_list.deleteCurrNode(link_list.head.next.next.next.next)
    print "deleting the 5th node"
    print link_list

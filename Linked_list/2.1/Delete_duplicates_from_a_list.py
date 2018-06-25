import sys
sys.path.append("../linked_list_class")
from singly_linked_list_class import *

def del_duplicate(link_list):
    head = link_list.head
    hash_list = [False]*256
    while head is not None:
        if hash_list[ord(head.data)] is True:
            if head.next is None:
                link_list.deleteLastNode()
                head = head.next
            else:
                link_list.deleteCurrNode(head)
        else:
            hash_list[ord(head.data)] = True
            head = head.next

    return link_list


if __name__ == '__main__':
    link_list = SinglyLinkedList()
    d = "dN9c0ODx1Lbi6i9hDlfPsFrqrOOqfYBSOSPyCyUaId1dge7uWRYEpXl8ZuwmZcyrSiSf" +\
    "wsCBxNvJjgRfwGLxfye8cjwIPXGM5KUr3xyJJX8fUxwaG3lnJjiWsybNzOD0a90eD3vVRV8p" +\
    "QKHxole75AZnm8GyeTIhxWB0uckEqPhm190sdTySkxhT5PMeJSoxf3y5u9D0foGYjFclYQ9XxLDkAmg4AAPZVxR8rfYoyGW0gxfFXwAEXKjHatATxxmFqINBPRS4IrFGfxxdc7uPYC485ym9iBKPAcCZFjd0BC34EaarSFo91PW0yiPvN1TmvcUmFRD4HPpVt3T3HTl4wyB4j60LdrVm68WfLNvAFQlRf7kD6I4QWzz6AoiTk9rtBtUXDJ5RTmdnFP7ELqrU5dfYsbl4gcFAh68WXd2n3qiyDnNymIjKMrD5D1wBDqOLpNMChOZ5X48f4lgj0LpHD11n6E9JtmMtqmtrfUJRX8cz4mxAdM283x9plmRG4c6SdhG1ND1SR8I8RWFpIfjVjsXqDfK4MoTgSzEkkk9w5dCYb1tau8mbxbBKgb4OQVpQ9M5nitbRNPLI4XoFJJDk4TGy6ZFjakFQyGN5GOFzEjPX5BPgiL4VDXOyLU8teHAenn9tItEIv4teBQJV4aiLnuQoAUckFiMIQetXXKkWZEBFEHmURRSo1Nb1OqxEasWJ1HgaFGMy60RJjznFoqZEALgw72PRkZPIYtmBbiKvorVvwip8vTZif8shxmlDNIyF3aX1TeeasBulLQ0BuoPkwMnD8Q3qW7vSvPTvIuCj9vUnTU1gV7fNcANAiVdmMYTSX4cmdtkHtVuu5u8w0vc5xFkSmOXz4x7VZiHxiKcOMONZBcF4BXONYHjJjIHTG77R1AaqtJVF02EBsBV95sLL8MXLzkrmAQ8ivzak4TWxiBGLjLjHamGPFyZaBOxeQzeitWx8hZRCWeUSKNMMTdMPkdsfgrCSLOjzG"
    for letter in d:
        link_list.insertNodeAtTail(letter)
    #print "the inputed link list is"
    #print link_list
    print "linked list after removing duplicates is"
    print(del_duplicate(link_list))

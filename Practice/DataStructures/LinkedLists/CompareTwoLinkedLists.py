#!/bin/python3

import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    v=1
    if llist1 is None and llist2 is None:
        return 1
    elif (llist1 is None and llist2 is not None) or (llist2 is None and llist1 is not None):
        return 0
    elif llist1.data == llist2.data:
        v *= compare_lists(llist1.next, llist2.next)
        return v
    else:
        return 0


if __name__ == '__main__':

#!/usr/bin/env python

class Node(object):
    def __init__(self, value):
        self.value = value 
        self.next = None
    
    def display(self, root):
        current = root 
        while current:
            print(current.value)
            current = current.next
    
    def insert(self, root, value ):
        if root == None:
            root = Node(value)

        elif root.next == None:
            root.next = Node(value)

        else:
            self.insert(root.next, value)
        return root


if __name__ == "__main__":
    d = Node(0)
    head = d.insert(d,2)
    d = Node(0)
    head = d.insert(d,1)
    head = d.insert(d,2)
    head = d.insert(d,3)
    head = d.insert(d,4)
    d.display(head)




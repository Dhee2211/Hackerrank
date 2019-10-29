#!/usr/bin/env python

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def insert(self, root, value):
        if root == None: 
            Node(value)
    
        while root != None:
            root = root.next







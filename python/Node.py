#!/usr/bin/python

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    def insert(self,data):
        if self.data > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
            
    def search(self,data):
        if self.data < data:
            if self.right == None:
                print 'Sorry, node %d is not fount.' %data
                return None
            else:
                self.right.search(data)
        elif self.data > data:
            if self.left == None:
                print 'Sorry, node %d is not found.'  %data
            else:
                self.left.search(data)
        else:
            print 'Yeah, node %d is found!' %data
            return self,parent

   def count_children(self):
       count = 0
       if self.left:
           count +=1
       if self.right:
           count +=1
       return count

    def delete(self,data):
        node, parent = self.search(data)
        if not node:
            return None
        else:
            children_num = node.count_children()
            if children_num == 0:
                if parent.left == node:
                    parent.left ==None
                else:
                    parent.right == None
                del node
            elif children_num == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent.left == node:
                    parent.left = n
                else :
                    parent.right = n
                del node
            else:
                temp = node
                successor = node.right
                while successor.left:
                    temp = successor
                    successor =successor.left
                if successor.right:
                    temp.left = successor.right
                    node.data = successor.data
                else :
                    temp.left = None
                    node.data = successor.data
                del successor
    def preorder_print(self):
        print self.data
        if self.left:
            self.left.preorder_print()
        if self.right:
            self.right.preorder_print()

    def inorder_print(self):
        if self.left:
            self.left.inorder_print()
        print self.data
        if self.right:
            self.right.inorder_print()

    def postorder_print(self):
        if self.left:
            self.left.postorder_print()
        if self.right:
            self.right.postorder_print()
        print self.data


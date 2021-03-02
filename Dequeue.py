# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:25:30 2021

@author: grass
"""
class Deque:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def addRear(self, item):
        self.items.append(item)
        
    def addFront(self, item):
        self.items.insert(0, item)
        
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
d = Deque()
print(d.isEmpty())
d.addRear(1)
d.addRear(2)
d.addFront(3)
d.addFront(4)
print(d.items)
d.removeFront
d.addFront(5)
d.removeRear
d.addRear(6)
print(d.items)
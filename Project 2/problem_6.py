# -*- coding: utf-8 -*-

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def values(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def contains(self, value):
        for value_ in self.values():
            if value == value_:
                return True
        return False

def union(llist_1, llist_2):
    union = LinkedList()
    
    for value in llist_1.values():
        if not union.contains(value):
            union.append(value)
    for value in llist_2.values():
        if not union.contains(value):
            union.append(value)
    return union

def intersection(llist_1, llist_2):
    intersection = LinkedList()
    
    for value in llist_1.values():
        if llist_2.contains(value):
            if not intersection.contains(value):
                intersection.append(value)
    return intersection


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
#Union: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
print (intersection(linked_list_1,linked_list_2))
#Intersection: 4 -> 6 -> 21 ->


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# Union: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_3,linked_list_4))
# Inersection: 

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
element_1 = [1,2,3,4,5,6,7,8,9,10]
element_2 = [10,9,8,7,6,5,4,3,2,1]

for i in element_1:
    linked_list_5.append(i)
for i in element_2:
    linked_list_6.append(i)


print(union(linked_list_5,linked_list_6))
#Union: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 
print(intersection(linked_list_5,linked_list_6))
#Intersection:	1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 

# Test case 4

empty_list = LinkedList()

print('Empty List:\t\t', empty_list)
#Empty List:		  
print('Empty List:\t\t', empty_list)
#Empty List:		 
print('Union:\t\t', union(empty_list,empty_list))
#Union:		 
print('Intersection:\t', intersection(empty_list,empty_list))
#Intersection:	
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

#Time Complexity = O(1)
#Space Complexity = O(1)

# class LinkedList:  #this create a empty linked list with no node
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 1

#Time Complexity = O(1)
#Space Complexity = O(1)

new_linked_list = LinkedList(10)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.length)
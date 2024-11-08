class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ' '
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result +=  ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def Prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index > self.length:  #Checking for range of link list
            return False
        if self.length == 0:    # if there is no link list
            self.head = new_node
            self.tail = new_node
        elif index == 0:         # if we are inserting at start
            new_node.next = self.head
            self.head = new_node
        else:                    # normal insertion at given index
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self,index):
        if index == -1:   #Return the last value on LinkedList
            return self.tail
        if index < -1 or index >= self.length:   # test case if there is negative index or value greater than length
            return None  
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value 
            return True
        return False
    
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
new_linked_list.set_value(2,50)
print(new_linked_list)

# Time Complexity = O(n)
# Space Complexity = O(1)
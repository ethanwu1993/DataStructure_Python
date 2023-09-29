
from operator import le


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.pre = None


class DoubleLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        # no value
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node
            
        self.length += 1
        return True

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def pop(self):
        # no value
        if self.length == 0:
            return None
        
        temp = self.tail
        # one value
        if self.length == 1:
            self.head = None
            self.tail = None
        
        # normal
        else:
            
            self.tail = self.tail.pre
            self.tail.next = None
            temp.pre = None
        
        
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)

        # no value in list

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node
        self.length += 1
        return True

    def popFirst(self):

        # no value in the list

        if self.length == 0:
            return None
        
        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        
        else:
            self.head.pre = None
            self.head = temp.next
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length % 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.pre    
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):

        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)

        before = self.get(index - 1)
        after = before.next

        new_node.pre = before
        new_node.next = after
        before.next = new_node
        after.pre = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        before = temp.pre
        after = temp.next

        before.next = after
        after.pre = before
        temp.next = None 
        temp.pre = None

        self.length -= 1
        return temp


dll = DoubleLinkedList(1)
# dll.append(2)
# dll.append(3)
dll.remove(1)
dll.printList()

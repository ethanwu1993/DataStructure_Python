

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print_list(self):
        temp = self.top

        while temp:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.top = new_node
        
        else:
            new_node.next = self.top
            self.top = new_node

        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.length -= 1
        return temp
    

s = Stack(4)
s.push(3)
print('pop', s.pop().value)
s.print_list()
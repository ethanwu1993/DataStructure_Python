class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
          self.tail.next = new_node
          self.tail = new_node

        self.length += 1
        return True

    def print(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def pop(self):

        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        pre.next = None
        self.tail = pre

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

        return True

    def pop_first(self):

        if self.length == 0:
            return None

        temp = self.head
        after = temp.next

        temp.next = None
        self.head = after
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):

        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):

        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False

    def insert(self, index, value):

        if index < 0 or index >= self.length:
            return False

        if index == 0:
            self.prepend(value)

        if index == self.length:
            self.append(value)

        new_node = Node(value)

        pre = self.get(index - 1)
        temp = self.get(index)

        pre.next = new_node
        new_node.next = temp

        self.length += 1
        return True


ll = LinkedList(1)
ll.append(2)
ll.append(3)
print(ll.insert(3, 0))
ll.print()

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # create new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # create new node
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # add last item value
            self.tail.next = new_node
            # move tail
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):

        # edge case 1: no item in the list
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        # normal case

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        # edge case 2: only one item in the list
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value

    def prepend(self, value):
        # create new node
        new_node = Node(value)
        # add node to beginning
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
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self, index) -> Node:
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

        if index < 0 or index > self.length:
            return False

        if index == self.length:
            return self.append(value)

        if index == 0:
            return self.prepend(value)

        new_node = Node(value)

        temp = self.get(index)
        pre = self.get(index - 1)
        pre.next = new_node
        new_node.next = temp

        self.length += 1

        return True

    def remove(self, index):

        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        pre = self.get(index - 1)

        pre.next = temp.next

        temp.next = None
        self.length -= 1

        return temp.value

    def reverse(self):

        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
print(my_linked_list.insert(4, 0))
my_linked_list.print_list()

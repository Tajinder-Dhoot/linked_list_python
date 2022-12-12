print('Hello, world!')


class Node:
    """
    An object for storing a single node of a linked list
    Models 2 attributes - data value and the link(reference) to the next node in the linked list
    """
    value = None

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return "<Node Data Value: %s>" % self.value

    def printNextNodeValueOfNode(self):
        return "<next node value of a node: %s>" % self.next_node


class LinkedList:
    """
    Singly Linked List"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time as has to go through all items in the list
        """
        current_node = self.head
        count = 0

        while current_node:
            count += 1
            current_node = current_node.next_node

        return count

    def add(self, data):
        """
        Adds a new node at head of the list
        Takes O(1) runtime
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, target):
        """
        Search for the first node containing data that matches with target
        Takes O(n) runtime as has to go through all items in the list
        """

        current_node = self.head
        
        while current_node:
            if current_node.value is target:
                return current_node
            else:
                current_node = current_node.next_node
        
        return None

    def insert(self, data, index):
        """
        Inserts a new node containing data at any index
        Insertion takes o(1) time but finding the node at the insertion point takes o(n) time
        So, overall takes o(n) time
        """

        list_size = self.size()

        if index <= list_size:
            if index == 0:
                self.add(data)
            else:
                new_node = Node(data)
                current_node = self.head
                current_node_index = 0
                while current_node_index < list_size:
                    if current_node_index == index - 1:
                        new_node.next_node = current_node.next_node
                        current_node.next_node = new_node
                        break

                    current_node = current_node.next_node
                    current_node_index += 1
        else:
            print("index where new node is to be inserted exceeded the size of linked list")

    def remove(self,key):
        list_size = self.size()
        current_node = self.head
        prev_node = None
        found = False

        while current_node and not found:
            if current_node.value == key and current_node is self.head:
                self.head = current_node.next_node

                """
                the line of code in comments is not required, its just for understanding
                when head of the linked list is moved to another node, the current is no longer attached to next node
                
                current_node.next_node = None
                """
                
                found = True
            elif current_node.value == key:
                prev_node.next_node = current_node.next_node

                """
                next one line of code is not required, its just for understanding
                when head of the linked list is moved to another node, the current is no longer attached to next node

                current_node.next_node = None
                """
                
                found = True
            else:
                prev_node = current_node
                current_node = current_node.next_node

        return current_node

    def __repr__(self):
        """
        String representation of the list
        Takes O(n) runtime
        """

        nodes = []
        current_node = self.head

        while current_node:
            if current_node == self.head:
                nodes.append("[Head: %s]" % current_node.value)
            elif current_node.next_node == None:
                nodes.append("[Tail: %s]" % current_node.value)
            else:
                nodes.append("[%s]" % current_node.value)

            current_node = current_node.next_node

        return '-> '.join(nodes)

    def printNextNodeValuesOfANodeInLinkedList(self):
        list_size = self.size()
        current_node = self.head
        current_node_index = 0

        while current_node_index < list_size:
            print(current_node.printNextNodeValueOfNode())
            current_node = current_node.next_node
            current_node_index +=1




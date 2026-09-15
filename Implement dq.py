class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    # Insert at front
    def insert_front(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    # Insert at rear
    def insert_rear(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    # Delete from front
    def delete_front(self):
        if self.front is None:
            print("Deque is empty")
            return

        self.front = self.front.next

        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None

    # Delete from rear
    def delete_rear(self):
        if self.rear is None:
            print("Deque is empty")
            return

        self.rear = self.rear.prev

        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None

    # Display
    def display(self):
        temp = self.front

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Example
dq = Deque()

dq.insert_front(10)
dq.insert_front(20)
dq.insert_rear(30)
dq.insert_rear(40)

print("Deque:")
dq.display()

dq.delete_front()
dq.delete_rear()

print("After deletion:")
dq.display()
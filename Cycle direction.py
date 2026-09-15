# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to detect cycle
def cycle_direction(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Create nodes
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Create cycle
head.next.next.next.next = head.next


# Check cycle
if cycle_direction(head):
    print("Cycle exists")
else:
    print("No cycle")
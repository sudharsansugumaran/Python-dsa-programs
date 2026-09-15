class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def rotate(head, k):
    if head is None or head.next is None:
        return head

    # Find length
    length = 1
    temp = head

    while temp.next:
        temp = temp.next
        length += 1

    k = k % length

    if k == 0:
        return head

    # Make circular
    temp.next = head

    # Find new tail
    steps = length - k
    new_tail = head

    for _ in range(steps - 1):
        new_tail = new_tail.next

    # New head
    new_head = new_tail.next

    # Break the circle
    new_tail.next = None

    return new_head


def display(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


# Create linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original:")
display(head)

# Rotate by 2 positions
head = rotate(head, 2)

print("After rotation:")
display(head)
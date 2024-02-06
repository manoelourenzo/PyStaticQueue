class Queue:
    """
    Implementation of a circular queue with a fixed capacity.

    Attributes:
        capacity (int): Maximum capacity of the circular queue.
        size (int): Current number of elements in the queue.
        begin (int): Index of the front of the queue.
        end (int): Index of the rear of the queue.
        items (list): List to store elements in the circular queue.


    """

    def __init__(self, capacity):
        """
        Initializes a circular queue with the specified capacity.

        Args:
            capacity (int): Maximum capacity of the circular queue.
        """
        self.capacity = capacity
        self.size = 0
        self.begin = 0
        self.end = -1
        self.items = [None] * capacity

    def isEmpty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.size == 0

    def isFull(self):
        """
        Checks if the queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return self.size == self.capacity

    def enqueue(self, item):
        """
        Adds an element to the rear of the queue.

        Args:
            item: Element to be added to the queue.
        """
        if not self.isFull():
            self.end = (self.end + 1) % self.capacity
            self.items[self.end] = item
            self.size += 1

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        Returns:
            item: Element removed from the front of the queue.
        """
        if not self.isEmpty():
            removed_item = self.items[self.begin]
            self.begin = (self.begin + 1) % self.capacity
            self.size -= 1
            return removed_item

    def clear(self):
        """
        Clears the queue by creating a new empty list.
        """
        self.items = [None] * self.capacity
        self.size = 0
        self.begin = 0
        self.end = -1

    def showQueue(self):
        """
        Displays the elements in the circular queue.
        """
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print("Circular Queue Elements:")
            current_index = self.begin
            for _ in range(self.size):
                print("|", self.items[current_index], "|", end=" ")
                current_index = (current_index + 1) % self.capacity
            print("\n")

CAPACITY = 10


# maximum heap (root node will be the largest item)
class Heap:

    def __init__(self):
        # this is the actual number of items in the data structure
        self.head_size = 0
        # the underlying list data structure
        self.heap = [0]*CAPACITY

    def insert(self, item):

        # when the heap is full
        if self.head_size == CAPACITY:
            return

        self.heap[self.head_size] = item
        self.head_size = self.head_size + 1

        # check the heap properties
        self.fix_up(self.head_size-1)

    # starting with actual node we have inserted up to root node
    # we have to compare the values whether to make swap operations
    # logN it has O(logN) running time complexity
    def fix_up(self, index):

        parent_index = (index - 1) // 2

        # we consider all the items above till we hit the root node
        # if heap property violated then we swap the parent-child
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

            self.fix_up(parent_index)

    def get_max(self):
        _

        return self.heap[0]

    def poll(self):

        max_item = self.get_max()

        # Swap the root node with the last item and "heapify"
        self.heap[0], self.heap[self.head_size-1] = self.heap[self.head_size-1], self.heap[0]
        self.head_size = self.head_size - 1

        # make sure the heap is "heapify"
        self.fix_down(0)

    # starting with the root node downwards until the heap properties are no longer violated - O(logN)
    def fix_down(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2

        # in a max heap the parent is always greater than the children
        largest_index = index

        # looking for the largest (parent or left node)
        if index_left < self.head_size and self.heap[index_left] > self.heap[largest_index]:
            largest_index = index_left

        if index_right < self.head_size and self.heap[index_right] > self.heap[largest_index]:
            largest_index = index_right

        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)

    def heap_sort(self):

        for _ in range(self.head_size):
            max_item = self.poll()
            print(max_item)


if __name__ == "__main__":
     heap = Heap()
     heap.insert(5)
     heap.insert(92)
     heap.insert(3)
     heap.insert(4)
     heap.insert(2)

     heap.heap_sort()
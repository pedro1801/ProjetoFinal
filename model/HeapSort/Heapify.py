class Heapify:
    def __init__(self,arr,n,i):
        self.arr = arr
        self.n = n
        self.i = i

        def heapify(arr, n, i):
            largest = i  # Initialize largest as root
            l = 2 * i + 1  # left = 2*i + 1
            r = 2 * i + 2  # right = 2*i + 2

            # See if left child of root exists and is
            # greater than root

            if l < n and arr[i] < arr[l]:
                largest = l

            # See if right child of root exists and is
            # greater than root

            if r < n and arr[largest] < arr[r]:
                largest = r

            # Change root, if needed

            if largest != i:
                (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

                # Heapify the root.

                heapify(self.arr, self.n, self.l)

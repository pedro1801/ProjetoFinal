import model.HeapSort.Heapify as Heapify

class Heapsort:
    def __init__(self,arr):
        self.arr = arr

        def heapSort(arr):
            n = len(arr)

            # Build a maxheap.
            # Since last parent will be at ((n//2)-1) we can start at that location.

            for i in range(n // 2 - 1, -1, -1):
                Heapify.Heapify(arr, n, i)

            # One by one extract elements

            for i in range(n - 1, 0, -1):
                (arr[i], arr[0]) = (arr[0], arr[i])  # swap
                Heapify.Heapify(arr, i, 0)
import model.QuickSort.Dividir as Dividir

class QuickSort:
    def __init__(self,arr,l,h):
        self.arr = arr
        self.l = l
        self.h = h
        def quickSort(arr, l, h):
            if l < h:
                pi = Dividir.Dividir(arr, l, h).l
                quickSort(arr, l, pi - 1)
                quickSort(arr, pi + 1, h)
        quickSort(self.arr,self.l,self.h)
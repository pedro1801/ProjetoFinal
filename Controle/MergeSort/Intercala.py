import Controle.MergeSort.MergeSort as MergeSort
class Intercala:
    def __init__(self,arr,l,n):
        self.arr = arr
        self.l = l
        self.n = n
        def intercala(arr,l, r):
            if l < r:
                m = l+(r-l)//2
                intercala(arr, l, m)
                intercala(arr, m+1, r)
                MergeSort.MergeSort(arr, l, m, r)
        intercala(self.arr,self.l,self.n)
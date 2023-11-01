import model.QuickSort.Dividir as Dividir
class QuickSort:
    def __init__(self,arr,l,h,Nomes):
        self.arr = arr
        self.l = l
        self.h = h
        def quickSort(alist,first,last):
            #print("Dentro quickSort")
            if first<last:
                splitpoint = Dividir.Dividir(alist,first,last,Nomes).Retorno
                quickSort(alist,first,splitpoint-1)
                quickSort(alist,splitpoint+1,last)
        quickSort(self.arr,self.l,self.h)
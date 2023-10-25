import model.MergeSort.Intercala as Intercala
import model.QuickSort.quickSort as quickSort
import model.HeapSort.HeapSort as heapSort

class Controle2:
    def __init__(self,Valores):
        self.Valores = Valores
        global lista 
        if self.Valores == "Automático":
            lista=[0,1,5,7,9,10,2,3,1,15,20,19,18,34]
        if self.Valores == "Inserir":
            print("teste")
        if  self.Valores == "MergeSort":
            size = len(lista)
            Intercala.Intercala(lista, 0, size - 1)
        if self.Valores == "QuickSort":
            size = len(lista)
            quickSort.QuickSort(lista, 0, size - 1)
        if self.Valores == "HeapSort":
            heapSort.Heapsort(lista)
        if self.Valores == 1:
            print(lista)
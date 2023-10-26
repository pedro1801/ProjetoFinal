import model.MergeSort.Intercala as Intercala
import model.QuickSort.quickSort as quickSort
import model.HeapSort.HeapSort as heapSort

class Controle2:
    def __init__(self,ini,Valores,Valor_Nome,Valor_Codigo):
        self.ini = ini
        self.Valor_Nome = Valor_Nome
        self.Valor_Codigo = Valor_Codigo
        self.Valores = Valores
        global lista 
        global Clientes
        global Nome
        global Codigo

        if self.ini == 1:
            lista = []
            Clientes = {}

        if Valor_Nome != 0:
            Nome = self.Valor_Nome
        if Valor_Codigo !=0:
            Codigo = self.Valor_Codigo

        if self.Valores == "Automático":
            lista=[200,1,5,7,9,10,2,3,1,15,20,19,18,34]
        if self.Valores == "Inserir":
            lista1 = [(Codigo,Nome)]
            lista.append(lista1)
            Clientes.update(lista1)
            print(Clientes)
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
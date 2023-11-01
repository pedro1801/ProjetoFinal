import model.MergeSort.Intercala as Intercala
import model.QuickSort.quickSort as QuickSort
import model.HashTable.HashTable as HashTable
import random

class Controle2:
    def __init__(self,ini,Valores,Valor_Nome,Valor_Codigo):
        self.ini = ini
        self.Valor_Nome = Valor_Nome
        self.Valor_Codigo = Valor_Codigo
        self.Valores = Valores
        global hashTable
        global Lista_Nome 
        global Lista_Codigo
        global Nome
        global Codigo
        if self.ini == 1:
            Lista_Nome = []
            Lista_Codigo = []

        if Valor_Nome != 0:
            Nome = self.Valor_Nome
        if Valor_Codigo !=0:
            Codigo = self.Valor_Codigo
            Codigo = int(Codigo)
        if self.Valores == "Automático":
            Nomes = ["Joao","Jose","Antonio","Alex","Thierry","Leonardo","Pedro","Acacio","Fatima","Maria"]
            max_numero = 300
            numeros_nomes = [random.randint(0, len(Nomes)-1) for _ in range(max_numero)]
            Lista_Codigo = random.sample(range(0, max_numero), max_numero)
            for i in range(0,len(numeros_nomes)):
                Lista_Nome.append(Nomes[numeros_nomes[i]])
        if self.Valores == "Inserir":
            Lista_Nome.append(Nome)
            Lista_Codigo.append(Codigo)
        if  self.Valores == "MergeSort":
            size = len(Lista_Codigo)
            Intercala.Intercala(Lista_Codigo, 0, size - 1,Lista_Nome)
        if self.Valores == "QuickSort":
            size = len(Lista_Codigo)
            QuickSort.QuickSort(Lista_Codigo,0,size-1,Lista_Nome)
        if self.Valores == "HashTable":
            hashTable = HashTable.HashTable(10000)
            for i in range(0,len(Lista_Codigo)):
                hashTable.put(Lista_Codigo[i],Lista_Nome[i])
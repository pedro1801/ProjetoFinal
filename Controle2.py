import flet as ft
import Controle.MergeSort.Intercala as Intercala
import Controle.QuickSort.quickSort as quicksort
import Visao.InserirValores as Inserir
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
            Intercala.Intercala(lista,0,size - 1)
        if self.Valores == "QuickSort":
            size = len(lista)
            quicksort.QuickSort(lista,0,size - 1)
        if self.Valores == 1:
            print(lista)
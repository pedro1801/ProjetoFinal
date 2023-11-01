class Dividir:
    def __init__(self,arr,l,h,Nomes):
        self.Nomes = Nomes
        self.arr = arr
        self.l = l
        self.h = h
        def Dividi(alist,first,last,Nomes):
            #print("Dentro Dividi")
            pivotvalue = alist[first]

            leftmark = first+1
            rightmark = last

            done = False
            while not done:

                while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                    leftmark = leftmark + 1

                while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                    rightmark = rightmark -1

                if rightmark < leftmark:
                    done = True
                else:
                    temp = alist[leftmark]
                    alist[leftmark] = alist[rightmark]
                    alist[rightmark] = temp
                    temp2 = Nomes[leftmark]
                    Nomes[leftmark] = Nomes[rightmark]
                    Nomes[rightmark] = temp2


            temp = alist[first]
            alist[first] = alist[rightmark]
            alist[rightmark] = temp
            temp2 = Nomes[first]
            Nomes[first] = Nomes[rightmark]
            Nomes[rightmark] = temp2


            return rightmark
        self.Retorno = Dividi(self.arr,self.l,self.h,self.Nomes)
class MergeSort:
    def __init__(self,arr,l,m,r,Nome):
        self.Nome = Nome
        self.arr = arr
        self.l = l
        self.m = m
        self.r = r
        def merge(arr, l, m, r,Nome):
            n1 = m - l + 1
            n2 = r - m
            L = [0] * (n1)
            R = [0] * (n1)
            L2 = [0] * (n1)
            R2 = [0] * (n1)
            for i in range(0, n1):
                L[i] = arr[l + i]
                L2[i] = Nome[l + i]
                #print("L:",L)
                #print("l2:",L2)
                #input()
        
            for j in range(0, n2):
                R[j] = arr[m + 1 + j]
                R2[j] = Nome[m + 1 + j]
                #print("R:",R)
                #print("R2:",R2)
                #input()
            i = 0    
            j = 0     
            k = l     
        
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    Nome[k] = L2[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    Nome[k] = R2[j]
                    j += 1
                k += 1
        

            while i < n1:
                arr[k] = L[i]
                Nome[k] = L2[i]
                i += 1
                k += 1
        

            while j < n2:
                arr[k] = R[j]
                Nome[k] = R2[j]
                j += 1
                k += 1
        merge(self.arr,self.l,self.m,self.r,self.Nome)
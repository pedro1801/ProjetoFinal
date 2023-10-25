class MergeSort:
    def __init__(self,arr,l,m,r):
        self.arr = arr
        self.l = l
        self.m = m
        self.r = r
        def merge(arr, l, m, r):
            n1 = m - l + 1
            n2 = r - m
            L = [0] * (n1)
            R = [0] * (n2)
            for i in range(0, n1):
                L[i] = arr[l + i]
        
            for j in range(0, n2):
                R[j] = arr[m + 1 + j]
        
            i = 0    
            j = 0     
            k = l     
        
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
        

            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1
        

            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1
        merge(self.arr,self.l,self.m,self.r)
class Dividir:
    def __init__(self,arr,l,h):
        self.arr = arr
        self.l = l
        self.h = h
        def Dividi(arr, l, h):
            # choose the rightmost element as pivot
            pivot = arr[h]
        
            # pointer for greater element
            i = l - 1
        
            # traverse through all elements
            # compare each element with pivot
            for j in range(l, h):
                if arr[j] <= pivot:
        
                    # If element smaller than pivot is found
                    # swap it with the greater element pointed by i
                    i = i + 1
        
                    # Swapping element at i with element at j
                    (arr[i], arr[j]) = (arr[j], arr[i])
        
            # Swap the pivot element with the greater element specified by i
            (arr[i + 1], arr[h]) = (arr[h], arr[i + 1])
        
            # Return the position from where partition is done
            return i + 1
        Dividi(self.arr,self.l,self.h)
class heap():
    def __init__(self,arr):
        self.arr = arr
        heap.heapify(self)

    def heapify(self):
        n = len(self.arr)
        for i in range(n//2-1,-1,-1):
            heap.__heapify(self.arr, n, i)

    def __heapify(arr, n, i ):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if (left<n and arr[left] > arr[largest]):
            largest = left
        if (right<n and arr[right] > arr[largest]):
            largest = right
        if (largest != i):
            arr[i] , arr[largest] = arr[largest],arr[i]
            heap.__heapify(arr,n,largest)
            
    
arr = [10, 3 ,5,9 , 2 ,1,2 ]

h = heap(arr)
print(h.arr)
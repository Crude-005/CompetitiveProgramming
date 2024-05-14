def swap(arr,arr2,i,j):
    arr[i] , arr[j] = arr[j] , arr[i]
    arr2[i] , arr2[j] = arr2[j] , arr2[i]
    
def partition(array, array2, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            swap(array,array2,i,j)

    swap(array,array2,i+1,high)
    return i + 1

def quicksort(array, array2, low, high):
    if low < high:
        pi = partition(array, array2, low, high)
        quicksort(array, array2, low, pi - 1)
        quicksort(array,array2, pi + 1, high)


def indexSort(arr,n):
    arr2 = [0,]*n
    for i in range(n):
        arr2[i] = i    
    quicksort(arr,arr2,0,n-1)
    return arr2

if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    n = len(array)

    # Function call
    arr2 = indexSort(array, n)
    print(array)
    print(arr2)



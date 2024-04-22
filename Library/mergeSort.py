
# ====================================================================
# MERGE SORT
def __merge__(arr,l,m,r):
    left_array = arr[l:m+1]
    right_array = arr[m+1:r+1]
    i = 0
    j = 0
    k = l
    l_len = m - l + 1
    r_len = r - m

    while(i<l_len and j<r_len):
        if (left_array[i]<=right_array[j]):
            arr[k] = left_array[i]
            i+=1
        else:
            arr[k] = right_array[j]
            j+=1
        k+=1

    while(i<l_len):
        arr[k] = left_array[i]
        i+=1
        k+=1
    
    while(j<r_len):
        arr[k] = right_array[j]
        j+=1
        k+=1
    return

def __mergeSortAlgo__(arr,l,r):
    if l >= r:
        return
    m = l+ (r-l)//2
    __mergeSortAlgo__(arr,l,m)
    __mergeSortAlgo__(arr,m+1,r)
    __merge__(arr,l,m,r)

def mergeSort(arr,n):
    __mergeSortAlgo__(arr,0,n-1)
    return

# ====================================================================



arr = [4, 23, 4, 62, 14, 1, 124, 231, 23141, 5235, 3, 21, 3, 2]
n = 14

print(arr)
mergeSort(arr,n)
print(arr)
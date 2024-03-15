def closest_city(arr,n):
    arr2 = [1,]*n
    for i in range(1,n-1):
        if arr[i]-arr[i-1] > arr[i+1]-arr[i]:
            arr2[i] = i+1
        else: arr2[i] = i-1
    arr2[-1] = n-2
    return arr2

def minimum_val(arr,arr2,curr,dest):
    money = 0
    inc = 1 if curr<dest else -1
    for curr in range(curr,dest,inc):
        if arr2[curr] == curr+inc:
            money+=1
        else:
            money+=abs(arr[curr]-arr[curr+inc])
    return money


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr2 = closest_city(arr,n)
    for _i_ in range(int(input())):
        start , end = map(int,input().split())
        print(minimum_val(arr,arr2,start-1,end-1))

        
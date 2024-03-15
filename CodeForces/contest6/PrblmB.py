def fn(arr,n):
    for i in range(n-2):
        if arr[i] <0:
            print("NO")
            return
        arr[i+1] -= arr[i]*2
        arr[i+2] -= arr[i]
    if arr[-2] !=0 or arr[-1] != 0:
        print("NO")
        return
    else:
        print("YES")
        return



for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    fn(arr,n)


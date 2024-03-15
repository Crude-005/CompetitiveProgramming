def fn(arr1,n,dis,dir):
    arr2 = [0,]*n
    if dir == '?':
        for i in range(n):
            if arr1[i]:
                arr2[(i+int(dis))%n] = 1
                arr2[(i-int(dis))%n] = 1
    elif dir == '0':
        for i in range(n):
            if arr1[i]:
                arr2[(i+int(dis))%n] = 1
    else:
        for i in range(n):
            if arr1[i]:
                arr2[(i-int(dis))%n] = 1
    return arr2
                



for _ in range(int(input())):
    n,m,x = map(int,(input().split()))
    arr1 = [0,]*n
    arr1[x-1] = 1
    for i in range(m):
        dis , dir = input().split()
        arr1 = fn(arr1,n,dis,dir)
    l = []
    for i in range(n):
        if arr1[i]:
            l.append(i+1)
    print(len(l))
    print(*l)

for _ in range(int(input())):
    n = int(input())
    arr =[]
    for i in range(n):
        if i&1:
            arr.append(i-249)
        else:arr.append(i-251)
    print(*arr)    
    
#level 1363
# time 30:12
# discovering algo
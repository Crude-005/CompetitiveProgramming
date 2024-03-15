for _ in range(int(input())):
    n,m,k = map(int,input().split())
    l1 = sorted(list(map(int,input().split())))
    l2 = sorted(list(map(int,input().split())))

    cnt = 0

    for i in l1:
        for j in l2:
            if i+j<=k:
                cnt+=1
            else:
                continue
    print(cnt)
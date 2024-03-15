for _ in range(int(input())):
    n,m = map(int,input().split())
    l1 = list(map(int,input().split()))
    l1.sort()
    l2 = sorted(list(map(int,input().split())))
    l2.reverse()
    i=0
    k = 1
    j = n if n<m else m
    sum = 0
    while(j>i):
        if abs(l2[i]-l1[i])>abs(l1[n-k]-l2[m-k]):
            sum+=abs(l2[i]-l1[i])
            i+=1
        else:
            sum+=abs(l1[n-k]-l2[m-k])
            k+=1
            j-=1
    print(sum)








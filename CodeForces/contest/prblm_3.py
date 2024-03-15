for _ in range(int(input())):
    n,f,a,b = map(int,input().split())
    l1 =list(map(int,input().split()))
    prev = 0
    for i in range(n):
        if (l1[i] - prev)*a < b:
            f-= (l1[i] - prev)*a
        else: f-=b
        prev=l1[i]
        i+=1
    print("YES" if f>0 else "NO")
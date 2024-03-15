for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    d = list(map(int,input().split()))
    survivors_def = []
    for i in range(n-1):
        if d[i] > a[i-1] + a[i+1]:
            survivors_def.append(d[i])
    else:
        if d[-1] > a[-2] + a[0]:
            survivors_def.append(d[-1])
    
    if(survivors_def):print(max(survivors_def))
    else: print(-1)


    # level 1397
    # total time    33:54
    # silly mistake in code
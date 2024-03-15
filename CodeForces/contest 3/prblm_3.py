from Collections import Counter
for _ in range(int(input())):
    n , m , k = map(int,input().split())
    l1 = sorted(list(map(int,input().split())))
    l2 = sorted(list(map(int,input().split())))
    cnt_n = 0
    cnt_m = 0
    buffer = 0
    
    if buffer+cnt_n+cnt_m == k and cnt_m<=k/2 and cnt_n<=k/2:
        print('YES')
    else:
        print('NO')
        

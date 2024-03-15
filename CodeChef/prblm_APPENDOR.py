for i in range(int(input())):
    N, Y = map(int,input().split())
    l1 = list(map(int,input().split()))
    f_or = 0
    for k in range(N):
        f_or = f_or | l1[k]
    m = f_or^Y
    if m == Y&m:
        print(m)
    else:
        print(-1)
 
#  level 1201
#  understanding: 2:21    2:21
#  formulating:   5:12    7:34
#  coding:        7:50    15:24
 
#            OPTIMISED

# for _ in range(int(input())):
#     n, y = map(int,input().split())
#     arr = list(map(int,input().split()))
#     oor = 0
#     for i in arr: oor |= i
#     req = oor^y
#     if req&y == m: print(m)
#     else: print(-1)     

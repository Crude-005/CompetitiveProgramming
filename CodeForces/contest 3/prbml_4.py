from collections import Counter

for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int,input().split()))
    for __ in range(int(input())):
        l , r = map(int,input().split())
        l2 = sorted(l1[l-1:r])
        if(max(l2) != min(l2)):
            print(l1.index(min(l2),l-1,r)+1,l1.index(max(l2),l-1,r)+1)
        else:
            print(-1,-1)
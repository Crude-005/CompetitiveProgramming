# 445A
n,m = map(int,input().split())
l1 = []
for i in range(n):
    l = list(input())
    for j in range(m):
        if l[j] == '.':
            if (i+j) & 1:
                l[j] = 'W'
            else:
                l[j] = 'B'
    l1.append(l)
for i in l1:
    print(''.join(i))
m,n = map(int,input().split())
soldiers = list(map(int,input().split()))
monsters = list(map(int,input().split()))

p = [0,0,0,1]
length = 4



list_use = [None,]*n
ind = 0

for j in range(n):
    if soldiers[j] > soldiers[p[2]] :
        p[3] = p[2]
        p[2] = j
    elif soldiers[j] > soldiers[p[3]]
        p[3] = j

list_use[0] = soldiers[p[2]]
list_use[1] = soldiers[p[3]]+list_use[0]
ind = 2

m = sum[soldiers[:3]]

for j in range(n-2):
    if sum[soldiers[j:j+3]] > m :
        p[0] = j 
        p[1] = j+3

list_use[ind] = list_use[ind-1]+m

if p[2] >= p[0] or p[2] <= p[0]:
    p[2] = None
if p[3] >= p[0] or p[3] <= p[0]:
    p[3] = None

if p[0] != 0 and p[1] !=n:
    if soldiers[p[1]+1] > soldiers[p[0] - 1]:
        p[1]




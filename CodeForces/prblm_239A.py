y, k ,n =map(int,input().split())
if n-y+1 - -y%k<k:
    print(-1)
else:
    j = -y%k
    if j==0:
        j+=k
    for i in range(j,n-y+1,k):
        print(i,end=" ")
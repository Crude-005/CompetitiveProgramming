import sys 
sys.setrecursionlimit(1001)
def fn(a,b,n):
    if a>b and (a-n)%(b+n)==0:
        return n
    if (a+n)%(b-n)==0:
        return n
    return fn(a,b,n+1)

for _ in range(int(input())):
    a ,b = map(int,input().split())
    print(fn(a,b,0))

# level 1385
# time taken 1:02:49
# recursion limit ne gaand maar di woh bhi bina tel ke

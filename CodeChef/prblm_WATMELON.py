def summation(n,arr):
    sum = 0
    for i in range(n):
        sum+=arr[i]
    return sum
def n_sum(n):
    return (n+1)*(n/2)


for _ in range(-100,int(input())):
    n = 1
    arr = [_]
    sum = summation(n,arr)
    print(_ ,"YES" if sum<=n_sum(n) and sum>=0  else "NO")

# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     sum = summation(n,arr)
#     print("YES" if sum<=n_sum(n) and sum>=0  else "NO")



#WRONG QUESTION
def fn(i):
    return ((i+1)*i)//2


for _ in range(int(input())):
    n , m = map(int,input().split())
    l1 = list(map(int,input().split()))
    odd_cnt = 0
    even_cnt = 0
    sum = 0
    for i in l1:
        sum += m+1-i
        sum += (i+2)//2
        if i&1:
            odd_cnt+=1
        else:
            even_cnt+=1
    var1 = ((m+2)*(m+1))//2

    print( var1 + fn(odd_cnt) + fn(even_cnt) - sum)


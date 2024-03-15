def fn(n):
    return int((n*(n-1)*(n-2))/6)

def fn2(n):
    return int(((n-1)*n)/2)
for _ in range(int(input())):

    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if n<3:
        print(0)
        continue
    if arr[0] == arr[-1]:
        print(fn(n))
        continue
    cnt= 0 
    prev_cnt = 0
    curr_cnt = 1
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            curr_cnt+=1
        else:
            if curr_cnt>=3:
                cnt += fn2(curr_cnt)*prev_cnt+fn(curr_cnt)
            elif curr_cnt == 2:
                cnt+=(fn2(curr_cnt)*prev_cnt)
            curr_cnt =1                
            prev_cnt = i+1
    else:
        if curr_cnt>=3:
            cnt +=(( fn2(curr_cnt) * prev_cnt) +fn(curr_cnt))
        elif curr_cnt == 2:
            cnt = cnt +  ((fn2(curr_cnt)) * prev_cnt)
    print(cnt)

# def function(n,data):
#     length = 2*n
#     i = 0
#     while(i<length):
#         if (data[i]&1):
#             n-=1
#             length-=1
#             data.pop(i)
#         else:i+=1
#     if (n<=0):
#         return 0-n
#     cnt = 0
#     exp = 1
#     i=0
#     while(n):
#         if((data[i]>>exp) & 1):
#             n-=1
#             length-=1
#             cnt+=exp
#             data.pop(i)
#         else:
#             i+=1
#         if(i==length):
#             i=0
#             exp+=1
#             print("3 first")
#     return cnt

# for _ in range(int(input())):
#     n = int(input())
#     data = list(map(int,input().split()))
#     print(function(n,data))

# time limt exceed in third case


# def function(n,data):
#     length = 2*n
#     i = 0
#     while(i<length):
#         if (data[i]&1):
#             n-=1
#             length-=1
#             data.pop(i)
#         else:i+=1
#     if (n<=0):
#         return 0-n
#     dick = {}
    

# for _ in range(int(input())):
#     n = int(input())
#     data = list(map(int,input().split()))
#     print(function(n,data))




def function(n,data):
    i = 0
    j = 2*n
    while(i<j):
        if (data[i]&1):
            n-=1
            data[i] ,data[j-1] = data[j-1],data[i]
            j-=1
        else:i+=1
    if (n<=0):
        return 0-n
    exp = 1
    cnt =0
    i=0
    while(n):
        print(f"n = {n},exp ={exp},cnt ={cnt},data[i] = {data},i={i},j = {j}")
        if(i<j):
            if((data[i]>>exp) & 1):
                print("yes it entered")
                n-=1
                cnt+=exp
                data[i] ,data[j-1] = data[j-1],data[i]
                j-=1
            else:
                i+=1
        else:
            i=0
            exp+=1
    return cnt
    

for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    print(function(n,data))

# level 1363
# time take 2h+
#logic and silly mistakes
    
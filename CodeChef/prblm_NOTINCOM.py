# for _ in range(int(input())):
#     n,m = map(int, input().split())
#     n_data = list(map(int,input().split()))
#     m_data = list(map(int,input().split()))
#     i = 0
#     cnt = 0
#     while(i<len(n_data)):
#         if n_data[i] in m_data:
#             cnt+=1
#             n_data.pop(i)
#         else:
#             i+=1
#     print(cnt)

# time limit exceeded





# for _ in range(int(input())):
#     n,m = map(int, input().split())
#     n_data = list(map(int,input().split()))
#     m_data = list(map(int,input().split()))
#     n_data.sort()
#     m_data.sort()
#     j = 0
#     i = 0
#     cnt = 0
#     while(True):
#         if j==m or i == n:
#             break
#         if n_data[i] == m_data[j]:
#             cnt+=1
#         elif i > m_data[j]:
#             j+=1
#         else:
#             i+=1
        
#     print (cnt)

for _ in range(int(input())):
    n,m = map(int, input().split())
    n_data = list(map(int,input().split()))
    m_data = list(map(int,input().split()))
    print(n+m-len(list(dict.fromkeys(n_data+m_data))))

# level 1386
# time taken    38:10

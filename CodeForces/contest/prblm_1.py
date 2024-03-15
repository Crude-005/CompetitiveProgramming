for _ in range(int(input())):
    l1 =[list(map(int,input().split())),
         list(map(int,input().split())),
         list(map(int,input().split())),
         list(map(int,input().split()))]
    for i in range(1,4):
        if l1[0][0] - l1[i][0] ==0:
            continue
        else:
            l1[0][0] = abs(l1[0][0]-l1[i][0])
            break
    for i in range(1,4):
        if l1[0][1] - l1[i][1]==0:
            continue
        else:
            l1[0][1] = abs(l1[0][1]-l1[i][1])
            break
    print(l1[0][0]*l1[0][1])
    
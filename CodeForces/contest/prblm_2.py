for _ in  range(int(input())):
    n = int(input())
    str1 = input()
    str2 = input()
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if int(str1[i])-int(str2[i]) == 1:
            cnt1 += 1
        elif int(str1[i])-int(str2[i]) == -1:
            cnt2 +=1
        else:
            pass
        
    print(cnt1 if cnt1>cnt2 else cnt2)
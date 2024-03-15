for _ in range(int(input())):
    n = int(input())
    str1 = input()
    cnt = 1
    for i in range(1,int(n/2)+1):
        if(str1[i:]+str1[:i] == str1):
            print(cnt)
            break
        else:
            cnt+=1
    else:
        print(n)
    


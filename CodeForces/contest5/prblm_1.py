for _ in range(int(input())):
    n = int(input())
    s = input()
    for i in range(int(n/2)):
        if(s[i]>s[n-(i+1)]):
            print(s[::-1]+s)
            break
        elif(s[i]<s[n-(i+1)]):
            print(s)
            break
    else:
        print(s)


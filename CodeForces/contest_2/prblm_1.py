for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    c = input()
    t_cnt= 0
    f_cnt =0
    for i in range(n):
        if a[i] == b[i] and c[i] !=a[i]:
            t_cnt+=1
        elif a[i] != b[i] and c[i]!=a[i] and b[i] != c[i]:
            t_cnt+=1
        else:
            f_cnt+=1
    print("YES" if t_cnt>=f_cnt else "NO")

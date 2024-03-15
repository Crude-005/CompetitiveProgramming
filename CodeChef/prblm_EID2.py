def fair_unfair(info):
    l1 = info[:3]
    l2 = info[3:6]
    for i in range(-1,2):
        if (l1[i]-l1[i+1] == 0 and l2[i]-l2[i+1] == 0) or (l1[i]-l1[i+1] > 0 and l2[i]-l2[i+1] > 0) or (l1[i]-l1[i+1] < 0 and l2[i]-l2[i+1]< 0):
            continue
        else:
            return False
    return True

for _ in range(int(input())):
    info = list(map(int,input().split()))
    if fair_unfair(info):
        print("FAIR")
    else:
        print("NOT FAIR")

# level 1378
# time 1:01:38
# concept ki chudi huyi hain
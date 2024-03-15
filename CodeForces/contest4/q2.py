for _ in range(int(input())):
    length = int(input())
    l1 = []
    for i in range(length):
        l1.append(input())

    square = True
    for j in range(length):
        cnt = l1[j].count('1')
        if cnt>0:
            if l1[j+1].count('1') - cnt != 0:
                square = False
            break

    print("SQUARE" if square else "TRIANGLE")


def main():
    for _ in range(int (input())):
        n = int(input())
        l1 = list(map(int,input().split()))
        cnt = l1.count(0)
        string = 'qwertyuiopasdfghjklzxcvbnm'
        l2 = [0,]*cnt
        s =''
        for i in l1:
            ind = l2.index(i)
            l2[ind]+=1
            s += string[ind]
        print(s)           

    return
    
if __name__ == '__main__':
    main()
        
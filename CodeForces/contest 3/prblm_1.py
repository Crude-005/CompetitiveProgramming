def main():
    for _ in range(int(input())):
        n = int(input())
        str1 = input()
        print((n - str1.index('B') - str1[::-1].index('B')))
    return
    
if __name__ == '__main__':
    main()
        
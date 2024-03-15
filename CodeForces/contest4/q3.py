def s(num):
    return (num+1)*num/2


def fn(num):
    if num == '':
        return 0
    return int(num)


for _ in range(int(input())):
    num = input()[::-1]
    sum = 0
    pow = 1
    for i in range(len(num)):
        prev = fn(num[:i][::-1])
        next = fn(num[i+1:][::-1])
        onit = fn(num[i][::-1])

        sum += (next * 45 + s(onit-1))*pow +  onit * (prev+1)
        pow *= 10

    print(int(sum))



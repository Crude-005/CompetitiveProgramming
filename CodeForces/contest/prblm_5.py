for _ in range(int(input())):
    h , w , x1 , y1,x2,y2 = map(int,input().split())
    if (x2-x1)&1:
        wall = 1 if y2<y1 else w
        if abs(wall-y2)<abs(y1-y2):
            print("Draw3")
        elif abs(y1-y2)/2<abs(x1-x2):
            print("Draw 4")
        else:print("Alice")
    else:
        wall = 1 if y2>y1 else w
        if abs(wall-y1)<abs(y1-y2):
            print("Draw 1")
        elif abs(y1-y2)/2<abs(x1-x2):
            print("Draw 2")
        else:print("Bob")


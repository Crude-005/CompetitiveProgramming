x,y,z = 0,0,0
for i in range(int(input())):
     a,b,c = map(int,input().split())
     x+=a 
     y+=b
     z+=c
if x|y|z:
     print("NO")
else:
     print("YES")
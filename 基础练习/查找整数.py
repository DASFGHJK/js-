n=int(input())
l=list(map(int,input().split()))
a=int(input())
count=0
for i in range(n):
    if a==l[i]:
        print(i+1)
        count+=1
        break
if i==n-1 and count==0:
    print(-1) //
l=int(input())
count=0
for i in range(l):
    n,m=map(int,input().split())
    for i in range(1,m+1):
        for j in range(1,n):
            if n%i==n%j:
                print("yes")
                count += 1
                break
if count==0:
    print("no")
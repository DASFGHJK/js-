n=int(input())
if n>=1 and n<=200:
    s1=list(map(int,input().split()))
    s1.sort()  #进行排序
    for i in range(len(s1)):
            print(s1[i],end=' ')

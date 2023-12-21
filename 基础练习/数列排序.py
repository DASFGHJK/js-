n=int(input()) #输入n
if n>=1 and n<=200:
    s1=list(map(int,input().split())) #进行每一行的分段
    s1.sort()   #将s1进行排序
    for i in range(len(s1)):  #由s1的长度进行排序
        print(s1[i],end=' ')
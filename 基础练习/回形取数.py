import math
r,c=map(int,input().split()) #输入对应的行号和列号
list1=[]
ans=[] #用来存放要进行术后如的函数
for i in range(0,r): #从深度来看
    list1.append(input().split())  #按照行来进行读入
for j in range(0,math.ceil(min(r,c)/2)):   #
    for x in range(j,r-j):  #行号按照倒叙进行输出
        ans.append(list1[x][j])  #输出对应行号和列号的数字区间
    for y in range(j+1,c-j): #将j圈的下一个一子项的x放入ans
        ans.append(list1[r-1-j][y])
    if c-1>2*j:
        for p in range[r-j-2,j-1,-1]:  #将j圈的1的数字放入ans
            ans.append(list1[p][c-1-j])
    if r-1>2*j:
        for q in range(r-j-2,j,-1):
            ans.append(list1[j][p])
for x in ans:
    print(x,'',end='')
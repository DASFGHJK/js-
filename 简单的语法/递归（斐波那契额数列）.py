n=int(input())  #实现一个数字的加入
F=[1,1]  #将F定义为一个数组
for i in range(n):
    F.append(F[i]+F[i+1])   #实现后一数字加上前一个数字
    # print(F[i])
#最
print(F[n-1])
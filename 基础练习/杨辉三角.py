n=int(input()) #输入第n行的杨辉三角
nums=[[0]*n for i in range (n)] # 初始化一个n*n的零阵
# print(nums)
for i in range(n):
    for j in range(n):  #进行列表的双循环
        if j==0: #将第一列的数字设置为1
            nums[i][j]=1 #将数列初始化
        else:
            nums[i][j]=nums[i-1][j]+nums[i-1][j-1]
        if nums[i][j]!=0:
            print(nums[i][j],end=' ')
    print( )  #实现换行的操作
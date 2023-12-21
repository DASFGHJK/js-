n=int(input())
for i in range(10000,1000000):
    #总共五或者六位数字
    a=str(i)
    b=0
    if a==a[::-1]: #判断是否为回文字符
        #如果是
        for j in a:
            b+=int(j) #将为一位进行拆分相加
            if b==n:
                print(a)
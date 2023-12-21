n=int(input())
if n<=10:  #如果符合条件
    for i in range(n):
        s=input() #输入n个十六进制的数字
        if(len(s)<=100000):
            res_1=int(s,16)  #先将16进制的数字转化为十进制的数字
            res_2=oct(res_1) #再将十进制转化为八进制
            print(res_2[2:])  #从第二个数字开始输出 因为八进制自动前面会有0o
    
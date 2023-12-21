# n=int(input())
# pi=list(map(int,input().split()))
# Count=[]
# if len(pi)==1:
#     count=pi  #此时列表中的长度为1
# while len(pi)!=1:
#     pi.sort(reverse=True)
#     a=pi.pop()
#     b=pi.pop()
#     Count.append(a+b)
#     pi.append(a+b)
# print(sum(Count))
n=int(input())
pi=list(map(int,input().split()))
count = []  #计算总共的值所需要保存你的数字
if len(pi)==1: #此时当pi数组只有一个数字
    count=pi #此时的对用数值就只有唯一一个值
while len(pi)!=1:  #当数组的长度不是1的时候进行循环
    pi.sort(reverse=True) #将pi数组进行倒叙的排列
    a=pi.pop() #取出最小的
    b=pi.pop() #取出次小的数字
    count.append(a+b) #将a和b相加的数字添加进求和数组
    pi.append(a+b) #病将相加之和添加进
print(sum(pi)) #最后将pi数组进行求和计算
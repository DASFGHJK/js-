import os
import sys
#题目总概括：统计在一个句子中出现最多的字母
n=input() #
li=[0]*200
for i in n:
    x=ord(i) #转化为ascill码值
    li[x]=li[x]+1 #对应的数值＋1
print(chr(list.index(max(li))))
print(max(li))

#知识点
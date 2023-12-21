# m,n=map(int ,input().split())
# str1=[] #str1为列表类型
# for i in range (m):
#     str1.append(chr(ord('A')+i))
# for j in range(n):
#     print(str1[j],end=' ')
# print()
# for k in range(1,n):
#     str1.insert(0,chr(ord('A')+k))
#     str1.pop()
#     for p in range(len(str1)):
#         print(str1[p],end=' ')
#     print()
m,n=map(int,input().split())
for i in range(m):
    for j in range(n):
        print(chr(65+abs(i-j)),end=' ')
    print()
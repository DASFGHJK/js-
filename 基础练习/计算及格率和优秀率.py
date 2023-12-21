n=int(input())
ji=0
you=0
for i in range(n):
    p=int(input())
    if p>=90:
        ji+=1
        you+=1
    if p>=60:
        ji+=1
o= int(float(ji)/n)*100
k=int(float(you)/n)*100
print(o"%")
print(k,"%")

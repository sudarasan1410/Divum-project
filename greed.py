a=[1,2,5]
b=11
count=0
d=[]
while b!=0:
    if b>=a[-1]:
        b=b-a[-1]
        count=count+1
    if b<a[-1]:
        d.append(a.pop())
print(count)
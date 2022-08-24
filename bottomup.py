coin=[1,2,3,5]
target=19
count=0
d=[]
i=[]
while target!=0:
    if target<=coin[0]:
        target=target-coin[0]
        count=count+1
        i.append(coin[0])
    if target>coin[0]:
        d.append(coin.pop(0))
print(count)
print(*i)
coin=[1,2,3,5]
target=19
count=0
d=[]
i=[]
while target!=0:
    if target>=coin[-1]:
        target=target-coin[-1]
        count=count+1
        i.append(coin[-1])
    if target<coin[-1]:
        d.append(coin.pop())
print(count)
print(*i)
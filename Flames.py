list=["a","b","c","d","e","f","g","h","i"]
a=4
count1=1
len=len(list)
i=0
while(list.count(' ')<len-1):
    if i==len:
        i=0
    if list[i]!=" ":
        if count1%a==0 or count1%10==a:
            count1+=1
            list[i]=" "
            
        if list[i]!=" ":
            count1+=1
    i=i+1
for k in list:
    if k!=" ":
        print(k)
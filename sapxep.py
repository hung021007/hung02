list = [2,6,3,8,1,4,7]
for i in range(0 ,len(list)-1):
    for j in range(i+1,len(list)):
        if(list[i]> list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list)
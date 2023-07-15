import numpy as np
s=input()
list1=[]
list2=np.zeros(len(s))
for i in s:
    list1+=[ord(i)]
for i in range(0,len(list1)-1):
    k=list1[i]
    if(k>=65 and k<=90) or (k>=97 and k<=122):
        if k%2==0 and (i+1)<len(list1) and list2[i+1]<1:
            a=list1[i+1]
            if not((a>=65 and a<=90) or (a>=97 and a<=122)):
                list1[i+1] =83
            else:
                list1[i+1] =list1[i+1]+(list1[i]%7)
                list2[i+1]+=1 
        else:
            if list2[i]!=2 and i!=0:
                a=list1[i-1]
                if not((a>=65 and a<=90) or (a>=97 and a<=122)):
                    list1[i-1] =83  
                else :  
                    list1[i-1]= list1[i-1]-(list1[i]%5)
                    list2[i-1]+=1
    else:
        list1[i]=83
for i in list1:
    print(chr(i), end='')

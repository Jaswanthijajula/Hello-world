s=input()
t=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        t.append(s[i:j])
x=int(input())
for i in t:
    if i[0]==i[-1]:
        if len(i)==x:
            print(i)

a,b=map(int,input("enter :").split())
c=0
while(a>0):
    if(a%b==0):
        print(a)   
        c=c+1
        break
    a=a//10
if(c==0):
    print("-1")

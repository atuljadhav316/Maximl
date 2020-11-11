#MT2019505 Atul Jadhav (IIITB)

s=input("Enter a string")
n= len(s)
ml=0
temp=""
ptr=0
cur=0
while ptr<(n-1):
    #print(temp,s[ptr])
    if s[ptr] not in temp:
        temp=temp+s[ptr]
        ptr+=1
    else:
        if ptr-cur+1>ml:
            ml=ptr-cur+1
        temp=""
        ptr=ptr+1
        cur=ptr-1           
print(ml)

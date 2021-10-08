# HARSHAD NUMBER

def harshad_number():
 sum=0
 n=int(input("not harshad number from 1 to : "))
 for i in range(1,n+1):
    temp=i
    while temp !=0:
        r=temp%10
        sum=sum+r
        temp=temp//10
    if i%sum!=0:
        print(i, end=" ")
    sum=0

harshad_number()
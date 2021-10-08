# Question 4

# input ka use kar ke 3 alag variables mein 3 integers ka input lein. 
# Input lene ke baad inn 3 mein se sabse bade number ko print karo 
# Note: Isme aap loops ka use nahi kar sakte.

num1=int(input("enter 1st no. "))
num2=int(input("enter 2n no. "))
num3=int(input("enter 3rd no. "))
if num1>num2 or num1>num3:
    print("GREATEST NO - ", num1)
elif num2>num1 or num2>num3:
    print("GREATEST NO - ", num2)
elif num3>num1 or num3>num2:
     print("GREATEST NO - ", num3)
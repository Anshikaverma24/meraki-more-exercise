# Pehle user se ek password ka string input lijiye.

# Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh
#  sab rule follow karne chaiye:
# Kam se kam uski length 6 honi chaiye
# Jada se jada length 16 se jyada na ho
# Kam se kam ek dollar ka sign ($) hona chaiye
# Kam se kam password mein 2 ya 8 hona chaiye
# Password mein capital A ya capital Z hona chaiye
# Agar password yeh rules follow kar raha hai toh "Strong Password" print karo, 
# nahi toh "Weak Password" type karo


# 
password=input("enter your password")
i=1
while i<=1:
 if len(password)<6:
    print("please increase the number of character in your password")
 if len(password)>16:
    print("please decrease the number of character in your password")
 if "$" not in password:
    print("please add $ sign in your password")
 if "8" or "2" not in password:
    print("please 8 or 2 in your password")
 if password=="A" or password=="Z" not in password:
    print(" please keep one letter capital")
 else:
     print("weak password")
 i+=1


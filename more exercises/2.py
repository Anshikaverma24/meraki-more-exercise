# Question 2

# Iss program mein hum students ki ginti aur ek student ke kharche se hisaab se 
# pure NavGurukul ka ek mahine ka kharcha nikalenge input ka use kar ke do values
#  ka input lo: 
# * Number of students
# * Ek student ka kharcha
# Iss ke hisaab se total kharcha nikalein. Agar total kharcha 50000 (50 hazar) ya
#  usse kam hai toh print karein "Hum budget ke andar hain" nahi toh print karo ki
#  hum budget ke bahar hain



no_of_stud=int(input("enter the number of students we have in navgurukul - "))
exp_of_one=int(input("enter the expenditure of one student - "))
total_exp=no_of_stud*exp_of_one
if total_exp<=50000:
    print("Hum budget ke andar hain")
else:
    print("hum budget ke bahar hain")

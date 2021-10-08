# Ab aap ek program likhoge jo ki user se ek integer input lega aur fir uska factorial
#  print karega. Agar user 3 dalega to 6 print karega, 7 dalega toh 5040 print karega aur
#  aise hi dusre numbers ke lie. Note: Abhi ke liye yeh soch lo ki user sirf positive integers 
# hi dalega. Negative integers kabhi nahi dalega.

times=int(input("enter the number of time you want to know factorial no."))
i=1
fac=1
while i<=times:
 userinput= int(input("enter the number"))
 fac=fac*userinput
 i+=1
print(fac)
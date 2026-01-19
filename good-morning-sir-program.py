name= input(" Enter Your Name :")
print(name)

import time
t=time.strftime("%H, %M, %S")
hour= int(time.strftime("%H"))
print(hour)

if(hour>0 and hour<12):
    print("Good Mornning ",name)

elif(hour>12 and hour<17):
    print("Good Afternoon " ,name)

elif(hour>17 and hour<21):
    print("Good Evinning ",name)

else:
    print("Good Night ",name)


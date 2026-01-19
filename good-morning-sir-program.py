import time
t=time.strftime("%H, %M, %S")
hour= int(time.strftime("%H"))
print(hour)

if(hour>0 and hour<12):
    print("Good Mornning Sir")

elif(hour>12 and hour<17):
    print("Good Afternoon Sir")

elif(hour>17 and hour<21):
    print("Good Evinning Sir")

else:
    print("Good Night Sir")


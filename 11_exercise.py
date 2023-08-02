import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)

if(timestamp >= '6:00:00' and timestamp <= '8:00:00'):
    print("Good Morning......Coffee is Ready🍵") 
elif(timestamp > '8:00:00' and timestamp <= '9:00:00'):
    print("Time to Have BreakFast🥣🍳")
elif(timestamp > '11:00:00' and timestamp <= '11:59:00'):
    print("Time to work something")
elif(timestamp >= '12:00:00' and timestamp <= '16:00:00'):
    print("Good Afternoon....")
elif(timestamp >= '16:00:00' and timestamp <= '18:00:00'):
    print("its a Tea Time...")
elif(timestamp >= '18:00:00' and timestamp <= '20:00:00'):
    print("its a relax and Snacks time")
elif(timestamp >= '20:00:00' and timestamp <= '22:00:00'):
    print("its Dinner Time...")
elif(timestamp >= '22:00:00' and timestamp <= '23:59:00'):
    print("its Movie And Chill time...")
elif(timestamp == '24:00:00'):
    print("time to sleep")
elif(timestamp >= 1 and timestamp <= 5):
    print("Early Morining...")
else:
    print("have a Good day...")

#To show AM/PM
if(timestamp >= '24:00:00' and timestamp <= '12:00:00'):
    print("The time is:",timestamp,"AM")
else:
    print("The time is:",timestamp,"PM")
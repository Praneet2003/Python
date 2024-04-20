import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp) 
timestramp = int(time.strftime('%H'))
print(timestramp)
timestramp = int(time.strftime('%M'))
print(timestramp)
timestamp = int(time.strftime('%S'))
print(timestramp)
if(timestramp>0 and timestramp<12):
    print("Good Morning Sir")
elif(timestramp>=12 and timestamp<18):
    print("Good Afternoon Sir")
elif(timestramp>=18 and timestamp<22):
    print("Good Evening Sir")
else:
    print("Good Night Sir")


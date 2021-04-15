from datetime import datetime
from playsound import playsound

time=input("Enter the time you want to set alarm on (HH:MM:SS) : ")
hr=time[0:2]
min=time[3:5]
sec=time[6:8]
print(hr+min+sec)

while True:
    now=datetime.now()
    current_hour = now.strftime('%I')
    current_minute = now.strftime('%M')
    current_second = now.strftime('%S')

    if(current_hour==hr):
        if(current_minute==min):
            if(current_second==sec):
                print('wake up')
                break


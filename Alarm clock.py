
import time
from playsound import playsound
CLEAR = "\033[2J"

def alarm(seconds):
    time_gone=0
    print(CLEAR)

    while time_gone<seconds:
        time.sleep(1)
        time_gone +=1

        time_left=seconds-time_gone
        minutes_left=time_left//60
        secomds_left=time_left%60

        print('Alarm will sound in {:02d}:{:02d}'.format(minutes_left,secomds_left),end='\r')

    playsound("Alarm.mp3")
    
print(CLEAR)
min=int(input('Please enter the minutes: '))
sec=int(input('Please enter the seconds: '))
T_sec=(min*60)+sec
alarm(T_sec)
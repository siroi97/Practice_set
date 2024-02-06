import time


Q1=input("This is a count down timer \n Please enter the time format \n press 'H' for hours. \n press 'M' for minutes.\n press'S' for seconds.")

q2=Q1.lower()

if q2=='h':
    hour=int(input("please enter the number of hours"))
    time1=hour*3600
elif q2=='m':
    min=int(input("please enter the number of min"))
    time1=min*60
elif q2=='s':
    sec=int(input("Please enter the second"))
    time1=sec
else:
    print("Please enter the options correctly")



while time1:
    hours=(time1//3600)
    min=(time1//60)%60
    sec=time1%60
    timer='{:02d}:{:02d}:{:02d}'.format(hours,min,sec)
    print(timer, end="\r")
    time.sleep(1)
    time1-=1
print('Times UP!!!')
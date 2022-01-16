import time
from playsound import playsound
t = 15
print("After 12 minutes Cooker will Off")

while t:
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}' .format(mins,secs)
    print("\r" +timer, end=' ')
    time.sleep(1)
    t= t-1
print("\nMummy, please switch off the Pressure Cooker")
playsound('mummy.mp3')

#Code for Advanced StopWatch
from machine import Pin
import time
import random
pb1=Pin(18,Pin.IN,Pin.PULL_UP)
pb2=Pin(32,Pin.IN,Pin.PULL_UP)
astro = Pin(25,Pin.OUT)
t=None
t1=None
s=None
s1=None
while True:
    pb1_val=pb1.value()
    pb2_val=pb2.value()
#IDLE STATE
    astro.on()
    time.sleep(0.1)
    astro.off()
    time.sleep(0.1)
#START GAME
    if pb1_val==0:
        astro.on()
        time.sleep(2)#to signal game is starting
        astro.off()
#REACTION TEST
        r=random.randint(1,5)
        print("delay is",r)
        time.sleep(r)
        astro.on() #after a random delay the led turns on
        s=time.ticks_ms()
        
        while pb1.value()==1:
            pass
        #if pb1_val==0:
            s1=time.ticks_ms()
            time.sleep(0.1)
        astro.off()
            #RESULT
        d=time.ticks_diff(s1,s)
        print("your reaction time was",d)
        time.sleep(0.2)
        
        time.sleep(5)

        
    
        



BLINKING OF LED CODE :

import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
while True:
 GPIO.output(8, GPIO.HIGH)
 sleep(1) 
 GPIO.output(8, GPIO.LOW) 
 sleep(1) 

TRAFFIC LIGHT CODE :

from gpiozero import Button, TrafficLights, Buzzer    
from time import sleep    
buzzer = Buzzer(15)    
button = Button(21)    
lights = TrafficLights(25, 8, 7)    
while True:    
           button.wait_for_press()   
           buzzer.on()   
           light.green.on()    
           sleep(1)    
           lights.amber.on()    
           sleep(1)    
           lights.red.on()    
           sleep(1)    
           lights.off()   
           buzzer.off()  

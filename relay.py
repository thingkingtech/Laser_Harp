import RPi.GPIO as GPIO
import time
import datetime 

button = 18
relay1 = 15
relay2 = 14
led = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup relays, LED and button
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Default mode for relays off, LED on
GPIO.output(relay1, GPIO.HIGH)
GPIO.output(relay2, GPIO.HIGH) 
GPIO.output(led, GPIO.HIGH)
time.sleep(1)

try:
    while True:
	time.sleep(0.1)
	push1=(GPIO.input(button))
	time.sleep(0.1)
	push2=(GPIO.input(button))
	time.sleep(0.1)
	push3=(GPIO.input(button))
	time.sleep(0.1)
	push4=(GPIO.input(button))
	time.sleep(0.1)
	push5=(GPIO.input(button))
	time.sleep(0.1)
	push6=(GPIO.input(button))

        if (push1 == 1 and push2 == 1 and push3 ==1 and push4==1 and push5==1 and push6==1):   # If Button is pushed
	    print("on")
	    start_time=datetime.datetime.now()
	    end_time = start_time + datetime.timedelta(minutes=10)
	    nownow = datetime.datetime.now()
	    while(end_time>nownow):
		    print("mist on")
	            GPIO.output(led, GPIO.LOW)          # Turn off LED inside button
       	    	    GPIO.output(relay1, GPIO.LOW)       # Trigger Relays
        	    GPIO.output(relay2, GPIO.LOW)
		    time.sleep(5)
		    print("mist off")
		    GPIO.output(relay2, GPIO.HIGH)
		    time.sleep(7)
		    nownow=datetime.datetime.now()
	    print("off")                         # Wait 10 minutes
            GPIO.output(relay1, GPIO.HIGH)      # Turn relays off
            GPIO.output(relay2, GPIO.HIGH)
            GPIO.output(led,GPIO.HIGH)          # Turn on LED inside button
	else:
	    GPIO.output(relay1, GPIO.HIGH)
	    GPIO.output(relay2, GPIO.HIGH)
	    GPIO.output(led, GPIO.HIGH)           
	
except KeyboardInterrupt:
        GPIO.output(relay1, GPIO.HIGH)
        GPIO.output(relay2, GPIO.HIGH) 
        GPIO.output(led, GPIO.HIGH) 
        GPIO.cleanup()


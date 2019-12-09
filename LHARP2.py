# Example for RC timing reading for Raspberry Pi
# using CircuitPython Libraries

import time 
from time import sleep
import board
from digitalio import DigitalInOut, Direction
import os
from pythonosc import osc_message_builder
from pythonosc import udp_client
import RPi.GPIO as GPIO

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

note1="C5"
note2="D5"
note3="E5"
note4="F5"
note5="G5"
note6="A5"
note7="B5"

note8="C3"
note9="D3"
note10="E3"
note11="F3"
note12="G3"
note13="A3"
note14="B3"

pin4 = 4
pin17 = 17
pin27 = 27
pin22 = 22
pin10 = 10
pin9 = 9
pin11 = 11

pin5 = 5
pin6 = 6
pin13 = 13
pin19 = 19
pin26 = 26
pin16 =16
pin21 = 21



GPIO.setmode(GPIO.BCM)

GPIO.setup(pin4, GPIO.IN)
GPIO.setup(pin17, GPIO.IN)
GPIO.setup(pin27, GPIO.IN)
GPIO.setup(pin22, GPIO.IN)
GPIO.setup(pin10, GPIO.IN)
GPIO.setup(pin9, GPIO.IN)
GPIO.setup(pin11, GPIO.IN)

GPIO.setup(pin5, GPIO.IN)
GPIO.setup(pin6, GPIO.IN)
GPIO.setup(pin13, GPIO.IN)
GPIO.setup(pin26, GPIO.IN)
GPIO.setup(pin16, GPIO.IN)
GPIO.setup(pin21, GPIO.IN)
GPIO.setup(pin19, GPIO.IN)

def playnote(note):
        sender.send_message('/play_this', note, )
        sleep(0.1)
        return 0
           

reading4_prev = 1
reading17_prev = 1
reading27_prev = 1
reading22_prev = 1
reading10_prev = 1
reading9_prev = 1
reading11_prev = 1

reading5_prev = 1
reading6_prev = 1
reading13_prev = 1
reading19_prev = 1
reading26_prev = 1
reading16_prev = 1
reading21_prev = 1
        
while True:
        
        reading11 = GPIO.input(11)
        reading4 = GPIO.input(4)
        reading17 = GPIO.input(17)
        reading27 = GPIO.input(27)
        reading22 = GPIO.input(22)
        reading10 = GPIO.input(10)
        reading9 = GPIO.input(9)
        
        reading5 = GPIO.input(5)
        reading6 = GPIO.input(6)
        reading13 = GPIO.input(13)
        reading19 = GPIO.input(19)
        reading26 = GPIO.input(26)
        reading16 = GPIO.input(16)
        reading21 = GPIO.input(21)
           
        if reading11 == 1 and reading11 != reading11_prev:
                playnote(note5)
                print("11 - note5")
        if reading4 == 1 and reading4 != reading4_prev:
                playnote(note11)
                print("4 - note11")
        if reading17 == 1 and reading17 != reading17_prev:
                print("17 - note12")
                playnote(note12)
        if reading27 == 1 and reading27 != reading27_prev:
                playnote(note14)
                print("27 - note14")
        if reading22 == 1 and reading22 != reading22_prev:
                playnote(note13)
                print("22 - note13")
        if reading10 == 1 and reading10 != reading10_prev:
                print("10 - note7")
                playnote(note7)
        if reading9 == 1 and reading9 != reading9_prev:
                print("9 - note6")
                playnote(note6)
        

        if reading5 == 1 and reading5 != reading5_prev:
                playnote(note2)
                print("5 - note2")
        if reading6 == 1 and reading6 != reading6_prev:
                playnote(note1)
                print("6 - note1")
        if reading13 == 1 and reading13 != reading13_prev:
                print("13 - note8")
                playnote(note8)
        if reading19 == 1 and reading19 != reading19_prev:
                playnote(note9)
                print("19 - note9")
        if reading26 == 1 and reading26 != reading26_prev:
                playnote(note10)
                print("26 - note10")
        if reading21 == 1 and reading21 != reading21_prev:
                print("21 - note3")
                playnote(note3)
        if reading16 == 1 and reading16 != reading16_prev:
                print("16 - note4")
                playnote(note4)
        
        reading4_prev = reading4
        reading17_prev = reading17
        reading27_prev = reading27
        reading22_prev = reading22
        reading10_prev = reading10
        reading9_prev = reading9
        reading11_prev = reading11
        
        reading5_prev = reading5
        reading6_prev = reading6
        reading13_prev = reading13
        reading19_prev = reading19
        reading26_prev = reading26
        reading16_prev = reading16
        reading21_prev = reading21

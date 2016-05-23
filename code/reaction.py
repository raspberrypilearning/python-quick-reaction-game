from gpiozero import LED, Button
from time import sleep
from random import uniform
import sys

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name is ')
right_name = input('right player name is ')

led.on()
sleep(uniform(1,2))
led.off()

def pressed(button):
    if button.pin.number == 14:
        print(left_name + ' won the game')
    else:
        print(right_name + ' won the game')
    sys.exit()

right_button.when_pressed=pressed
left_button.when_pressed=pressed


from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name is ')
right_name = input('right player name is ')

led.on()
sleep(uniform(5, 10))
led.off()

def pressed(button):
    print("{} won the game".format(button))

right_button.when_pressed(pressed(left_name))
left_button.when_pressed(pressed(right_name))


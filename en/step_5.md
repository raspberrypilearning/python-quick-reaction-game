## Detecting the buttons

The LED is working; now you want to add functionality to your program so that when a button is pressed it is detected. That way you can record the players' scores to see who wins.

As with the last step, some code needs to be added to your current program.

--- task ---
With the file **reaction.py** open add the following variables underneath `led = LED(4)`:

--- code ---
---
language: python
filename: reaction.py
line_numbers: true
line_number_start: 1
highlight_lines: 6-7
---
from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

led.on()
sleep(uniform(5, 10))
led.off()
--- /code ---

--- /task ---

--- task ---
Then underneath `led.off()` you can add a function that will be called whenever a button is pressed, which will tell you which **pin** the button was on:

--- code ---
---
language: python
filename: reaction.py
line_numbers: true
line_number_start: 1
highlight_lines: 14-15
---
from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

led.on()
sleep(uniform(5, 10))
led.off()


def pressed(button):
	print(str(button.pin.number) + ' won the game')
--- /code ---

--- /task ---

--- task ---
To finish off, when either button is pressed, the function will be called. If the `right_button` is pressed, then you can send the string `'right'` to the `pressed` function. If the `left_button` is pressed, then you can send the string `'left'`.

--- code ---
---
language: python
filename: reaction.py
line_numbers: true
line_number_start: 1
highlight_lines: 18-19
---
from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

led.on()
sleep(uniform(5, 10))
led.off()


def pressed(button):
	print(str(button.pin.number) + ' won the game')


right_button.when_pressed = pressed
left_button.when_pressed = pressed
--- /code ---

--- /task ---

--- task ---
Save your program and test it with a friend.
--- /task ---



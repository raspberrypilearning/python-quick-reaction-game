## Get player names

Wouldn't it be better if the program told you who has won instead of just which button was pressed? For this, you need to find out the players' names. In Python, you can use **input** for this.

--- task ---
To find out the names of the players you can use `input` to ask the players to type in their names. Underneath the imported libraries and modules, and the highlighted code.

--- code ---
---
language: python
filename: reaction.py
line_numbers: true
line_number_start: 1
highlight_lines: 9-10
---
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
	print(str(button.pin.number) + ' won the game')


right_button.when_pressed = pressed
left_button.when_pressed = pressed
--- /code ---

--- /task ---

--- task ---
Now you can rewrite your pressed function, so that it can print out the name of the player who won.

--- code ---
---
language: python
filename: reaction.py
line_numbers: true
line_number_start: 1
highlight_lines: 17-21
---
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
	if button.pin.number == 14:
		print(left_name + ' won the game')
	else:
		print(right_name + ' won the game')


right_button.when_pressed = pressed
left_button.when_pressed = pressed
--- /code ---

--- /task ---

--- task ---
Run your program and test your game to see if it works.
--- /task ---

--- task ---
You might notice that the game doesn't quit when the button has been pushed. This can be fixed by adding an exit into the `pressed` function. Add the highlighted lines to your code,

--- code ---
---
language: python
filename: reaction.py
line_numbers: true
line_number_start: 1
highlight_lines: 4, 23
---
from gpiozero import LED, Button
from time import sleep
from random import uniform
from sys import exit

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name is ')
right_name = input('right player name is ')

led.on()
sleep(uniform(5, 10))
led.off()


def pressed(button):
	if button.pin.number == 14:
		print(left_name + ' won the game')
	else:
		print(right_name + ' won the game')
	exit()


right_button.when_pressed = pressed
left_button.when_pressed = pressed
--- /code ---

--- /task ---


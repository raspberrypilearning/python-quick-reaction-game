## Adding an element of surprise

The object of the game is to see who can press the button first when the light goes out, so it would be better if the length of time it stayed on were random. You need to add and amend some lines of code in your Python program to make this happen.

--- task ---
Underneath `from time import sleep` add a line to import `uniform`

--- code ---
---
language: python
filename: reaction.py
line_numbers: true
line_number_start: 1
highlight_lines: 3
---
from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)

led.on()
sleep(5)
led.off()
--- /code ---

Here, `uniform` allows for the random selection of a decimal (floating point) number from a range of numbers.
--- /task ---

--- task ---
Then locate the line `sleep(5)` and amend it so that it reads:
--- code ---
---
language: python
filename: reaction.py
line_numbers: true
line_number_start: 1
highlight_lines: 8
---
from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)

led.on()
sleep(uniform(5, 10))
led.off()
--- /code ---
--- /task ---

--- task ---
Save your work by clicking on **Save**. Test that everything works by clicking on **Run**
--- /task ---


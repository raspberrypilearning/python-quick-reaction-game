## Controlling the light

When programming, it makes sense to tackle one problem at a time. This makes it easier to test your project at various stages.

--- task ---
Click on the  `Menu`>`Programming`>`Mu`
--- /task ---

--- task ---
Save the file as **reaction.py** by clicking on `File`>`Save As`
--- /task ---

--- task ---
First you will need to import the modules and libraries needed to control the GPIO pins on the Raspberry Pi. Type:
--- code ---
---
language: python
filename: reaction.py
line_numbers: true
line_number_start: 
highlight_lines: 
---
from gpiozero import LED, Button
from time import sleep
--- /code ---

--- /task ---

--- task ---
As you are outputting to an LED, you need to set up the pin that the LED connects to on the Raspberry Pi as an output. First use a variable to name the pin and then set the output:

--- code ---
---
language: python
filename: reaction.py
line_numbers: true
line_number_start: 
highlight_lines: 4
---
from gpiozero import LED, Button
from time import sleep

led = LED(4)
--- /code ---
--- /task ---
	
--- task ---
Next add a few lines to turn the LED on, wait for 5 seconds and then turn the LED off:

--- code ---
---
language: python
filename: reaction.py
line_numbers: true
line_number_start: 
highlight_lines: 6-8
---
from gpiozero import LED, Button
from time import sleep

led = LED(4)

led.on()
sleep(5)
led.off()
--- /code ---
--- /task ---

--- task ---
Finally, test that it works by click on `Run`.
--- /task ---

If the LED does not come on for five seconds, go back and see if you can work out what went wrong. This is a very important skill in computing called **debugging**, which means finding and fixing errors or bugs in your code.



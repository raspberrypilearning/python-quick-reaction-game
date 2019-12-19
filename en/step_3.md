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




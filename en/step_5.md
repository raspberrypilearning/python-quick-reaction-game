## Controlling the light

When programming, it makes sense to tackle one problem at a time. This makes it easier to test your project at various stages.

- Click on the  `Menu`>`Programming`>`Python 3 (IDLE)`

- Create a new text editor file by clicking on `File`>`New File`

- Save this file as **reaction.py** by clicking on `File`>`Save As`

- First you will need to import the modules and libraries needed to control the GPIO pins on the Raspberry Pi. Type:

	```python
	from gpiozero import LED, Button
	from time import sleep
	```

- As you are outputting to an LED, you need to set up the pin that the LED connects to on the Raspberry Pi as an output. First use a variable to name the pin and then set the output:

	```python
	led = LED(4)
	```
	
- Next add a line to turn the LED on:

	```python
	led.on()
	```
	
- Now add a line to wait 5 seconds by typing:

	```python
	sleep(5)
	```

- Then add a line to turn the LED off like this:

	```python
	led.off()
	```
- Save the file by clicking on `File`>`Save`.

- Finally, test that it works by click on `Run`>`Run Module` or by pressing `F5` on the keyboard.

If the LED does not come on for five seconds, go back and see if you can work out what went wrong. This is a very important skill in computing called **debugging**, which means finding and fixing errors or bugs in your code.



## Adding an element of surprise

The object of the game is to see who can press the button first when the light goes out, so it would be better if the length of time it stayed on were random. You need to add and amend some lines of code in your Python program to make this happen.

- If the file **reaction.py** is not already open in IDLE3 then open it by clicking on **File** and **Open**.

- Underneath `from time import sleep` add the following line:

	```python
	from random import uniform
	```
    Here, `uniform` allows for the random selection of a decimal (floating point) number from a range of numbers.
	
- Then locate the line `sleep(5)` and amend it so that it reads:

	```python
	sleep(uniform(5, 10))
	```

- Save your work by clicking on **File** and **Save**. Test that everything works by pressing `F5` to run your code.


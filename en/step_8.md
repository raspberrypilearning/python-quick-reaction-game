## Get player names

Wouldn't it be better if the program told you who has won instead of just which button was pressed? For this, you need to find out the players' names. In Python, you can use **input** for this.

- To find out the names of the players you can use `input` to ask the players to type in their names. Underneath the imported libraries and modules, type:

	```python
	left_name = input('left player name is ')
	right_name = input('right player name is ')
	```
- Now you can rewrite your pressed function, so that it can print out the name of the player who won.

	``` python
	def pressed(button):
		if button.pin.number == 14:
			print(left_name + ' won the game')
		else:
			print(right_name + ' won the game')
	```

- 	Save **reaction.py** and test your game to see if it works.

- You might notice that the game doesn't quit when the button has been pushed. This can be fixed by adding an exit into the `pressed` function. First, add the following line to your imports.

	``` python
	from sys import exit
	```

- Then you can call `exit()` within your `pressed` function, once the prints have been completed.

	``` python
	def pressed(button):
		if button.pin.number == 14:
			print(left_name + ' won the game')
		else:
			print(right_name + ' won the game')
		exit()
	```


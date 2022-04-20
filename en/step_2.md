## Building the circuit

This is the circuit you are going to build, consisting of two push-to-make buttons and an LED.

![](images/quick-reaction-circuit.png)

--- task ---
Take one of your tactile buttons and push it into the holes on your breadboard, with one set of legs on row **H** and one set of legs on row **J**.
--- /task ---

--- task ---
Repeat the last step with the second button, placing it at the other end of the breadboard on the same row.
--- /task ---

--- task ---
Place an LED with the longer leg above the ridge in the breadboard in **D16** and the shorter leg in **D15**. The numbering will depend on your breadboard so make sure that you check the diagram below.
--- /task ---

--- task ---
Next push one leg of the resistor into the same column (**15**) as the short leg of the resistor and the other leg into a hole along the blue strip.
--- /task ---

--- task ---
Now it's time to add the jumper wires. Start by taking two pin-to-pin jumper wires and placing one end in a hole next to the outside leg of the left hand button, and the other end in a hole along the blue strip. Repeat this step with the right hand button.
--- /task ---

--- task ---
Then with a pin-to-socket jumper wire, connect **GPIO14** to a hole on the breadboard in line with the other leg of the left hand button. Repeat this step for the right hand button, only this time connecting it to **GPIO15**.
--- /task ---

--- task ---
Using another pin-to-socket jumper wire, connect **GPIO4** to a hole on the breadboard in line with the long leg of the LED.
--- /task ---

--- task ---
Finally, connect a **GND** GPIO pin to the blue strip on the breadboard with the remaining pin-to-socket jumper wire.
--- /task ---


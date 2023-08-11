# CTkSpinbox
Spinbox extension for customtkinter (add-on)

<showcase_light>
<showcase_dark>

## Installation
```
pip install CTkSpinbox
```

## Usage
```
import customtkinter as ctk
from CTkSpinbox import *

def print_label(count):
  print(count)

window = ctk.CTk()
window.geometry('200x150')

spin_var = ctk.IntVar()
spinbox = CTkSpinbox(window,
          start_value = 10,
          min_value = 0,
          max_value = 20,
          scroll_value = 2,
          variable = spin_var,
          command = print_label)
spinbox.pack(expand = True)

window.mainloop()
```

## Arguments
| Parameter | Description |
|-----------| ------------|
| **master** | parent widget |
| width | set width of the listbox |
| height | set height of the listbox |
| start_value | set starting value of the counter |
| min_value | set the lowest value the counter can be set to|
| max_value | set the highest value the counter can be set to |
| step_value | set increment/decrement value of the buttons |
| scroll_value | set increment/decrement value of the scroll wheel |
| variable | set **CTk/Tk** variable to the counter |
| font | set the font of the counter and buttons |
| fg_color | set the foreground color of the spinbox frame |
| border_color | set the border color of the spinbox frame |
| text_color | set the text color of the the counter and buttons |
| button_color | set the foreground color of the buttons |
| button_hover_color | set the hover color of the buttons |
| border_width | set the border width of the spinbox frame |
| corner_radius | set the corner radius of the spinbox frame |
| button_corner_radius | set the corner radius of the buttons |
| command | calls a command with counter value as a parameter when the counter is incremented/decremented |

## Methods
- **.decrement_counter()** - decrements the counter value
- **.increment_counter()** - increments the counter value
- **.scroll(scroll)** - decrements/increments the counter value [use -1 to decrement and 1 to increment]
- **.get_count()** - returns the counter value
- **.set_count(value)** - sets the counter to a value
- **.disable()** - disables the increment/decrement buttons
- **.enable()** - enables the increment/decrement buttons
- **.bind(key, function)** - executes the function when the event key is triggered
- **.configure(kwargs)** - changes the parameters of the spinbox

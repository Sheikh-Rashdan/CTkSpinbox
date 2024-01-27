"""
Custom Spinbox For CustomTkinter
Author : Sheikh Rashdan
Version : 1.2
"""

import customtkinter as ctk

class CTkSpinbox(ctk.CTkFrame):
    def __init__(self,
                 master: any,
                 width: int = 100,                            # width of the frame
                 height: int = 40,                            # height of the frame
                 start_value: int = 0,                        
                 min_value: int = 0,
                 max_value: int = 100,
                 step_value: int = 1,
                 scroll_value: int = 5,
                 variable: any = None,
                 font: tuple = ('X', 20),
                 fg_color: str = None,
                 border_color: str = ('#AAA', '#555'),
                 text_color: str = ('Black', 'White'),
                 button_color: str = ('#BBB','#444'),
                 button_hover_color: str = ('#AAA', '#555'),
                 border_width: int = 2,
                 corner_radius: int = 5,
                 button_corner_radius: int = 5,
                 button_border_width: int = 2,
                 button_border_color: str = ('#AAA', '#555'),
                 command: any = None):
        super().__init__(master,
                         height = height,
                         width = width,
                         fg_color = fg_color,
                         border_color = border_color,
                         border_width = border_width,
                         corner_radius = corner_radius)

        # values
        self.start_value = max(min(start_value, max_value), min_value)       # start value must not exceed limits
        self.min_value = min_value
        self.max_value = max_value
        self.step_value = abs(step_value)
        self.scroll_value = abs(scroll_value)
        self.variable = variable
        if self.variable:
            self.variable.set(self.start_value)
        self.font = font
        self.text_color = text_color
        self.button_color = button_color
        self.button_hover_color = button_hover_color
        self.button_corner_radius = button_corner_radius 
        self.button_border_width = button_border_width
        self.button_border_color = button_border_color
        self.command = command

        # counter label
        self.counter_var = ctk.IntVar(value = self.start_value)
        self.counter = ctk.CTkLabel(self,
                                    text = 'Error',
                                    textvariable = self.counter_var,
                                    font = self.font,
                                    text_color = self.text_color)

        # decrement button
        self.decrement = ctk.CTkButton(self,
                                       text = '-',
                                       font = self.font,
                                       text_color = self.text_color,
                                       fg_color = self.button_color,
                                       hover_color = self.button_hover_color,
                                       text_color_disabled = '#888',
                                       corner_radius = self.button_corner_radius,
                                       border_width = self.button_border_width,
                                       border_color = self.button_border_color,
                                       command = self.decrement_counter)

        # increment button
        self.increment = ctk.CTkButton(self,
                                       text = '+',
                                       font = self.font,
                                       text_color = self.text_color,
                                       fg_color = self.button_color,
                                       hover_color = self.button_hover_color,
                                       text_color_disabled = '#888',
                                       corner_radius = self.button_corner_radius,
                                       border_width = self.button_border_width,
                                       border_color = self.button_border_color,
                                       command = self.increment_counter)
        
        # grid
        self.rowconfigure(0, weight = 1, uniform = 'X')
        self.columnconfigure((0,2), weight = 11, uniform = 'X')
        self.columnconfigure(1, weight = 10, uniform = 'X')
        self.grid_propagate(False)

        # layout
        self.decrement.grid(row = 0, column = 0, sticky = 'news', padx = (4,0), pady = 4)
        self.counter.grid(row = 0, column = 1, sticky = 'news', padx = 0, pady = 4)
        self.increment.grid(row = 0, column = 2, sticky = 'news', padx = (0,4), pady = 4)

        # scroll bind
        self.bind('<MouseWheel>', self.scroll)

    def decrement_counter(self):
        self.counter_var.set(max(self.min_value, self.counter_var.get()-self.step_value))
        if self.variable:
            self.variable.set(self.counter_var.get())
        if self.command:
            self.command(self.counter_var.get())

    def increment_counter(self):
        self.counter_var.set(min(self.max_value, self.counter_var.get()+self.step_value))
        if self.variable:
            self.variable.set(self.counter_var.get())
        if self.command:
            self.command(self.counter_var.get())

    def scroll(self, scroll):
        dirn = 1 if scroll.delta>0 else -1
        if dirn == -1:
            self.counter_var.set(max(self.min_value, self.counter_var.get()-self.scroll_value))
        else:
            self.counter_var.set(min(self.max_value, self.counter_var.get()+self.scroll_value))
        if self.variable:
            self.variable.set(self.counter_var.get())
        if self.command:
            self.command(self.counter_var.get())

    def get(self):
        return self.counter_var.get()
    
    def set(self, value):
        self.counter_var.set(max(min(value, self.max_value), self.min_value))
    
    def disable(self):
        self.increment.configure(state = 'disabled')
        self.decrement.configure(state = 'disabled')

    def enable(self):
        self.increment.configure(state = 'enabled')
        self.decrement.configure(state = 'enabled')

    def bind(self, key, function):
        # bind_all doesn't work :(
        super().bind(key, function)
        self.counter.bind(key, function)
        self.increment.bind(key, function)
        self.decrement.bind(key, function)

    def configure(self, **kwargs):
        
        # conditions
        for value in ['font', 'text_color', 'button_color', 'button_hover_color', 'button_corner_radius', 'button_border_color', 'button_border_width']:
            if value in kwargs:
                new_value = kwargs.pop(value)
                if value not in ['font', 'button_corner_radius']:
                    if value not in ['button_hover_color', 'button_color', 'button_corner_radius']:
                        exec(f"self.counter.configure({value} = '{new_value}')")
                    value = {'button_color' : 'fg_color'}[value] if value in ['button_color', 'button_corner_radius'] else value
                    exec(f"self.increment.configure({value} = '{new_value}')")
                    exec(f"self.decrement.configure({value} = '{new_value}')")
                else:
                    value = {'button_corner_radius' : 'corner_radius'}[value] if value in ['button_color', 'button_corner_radius'] else value
                    exec(f"self.increment.configure({value} = {new_value})")
                    exec(f"self.decrement.configure({value} = {new_value})")
                    if value == 'font':
                        exec(f"self.counter.configure({value} = {new_value})")

        for value in ['min_value', 'max_value', 'step_value', 'scroll_value', 'variable']:
            if value in kwargs:
                new_value = kwargs.pop(value)
                exec(f'self.{value} = {new_value}')

        if 'command' in kwargs:
            self.command = kwargs.pop('command')

        super().configure(**kwargs)

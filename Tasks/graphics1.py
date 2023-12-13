#!/usr/bin/python3
import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

app = tk.Tk()
app.title("Tkinter Example")

label = tk.Label(app, text="Welcome to Tkinter!")
label.pack()

button = tk.Button(app, text="Click me!", command=on_button_click)
button.pack()

app.mainloop()


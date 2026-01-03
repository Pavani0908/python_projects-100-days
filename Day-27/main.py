import tkinter as tk
import turtle
from tkinter import Entry

window = tk.Tk()
window.title("MY FIRST GUI PROGRAM")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I AM a label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.config(text="New Text")

# Button
def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)


button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

#entry
input = Entry(width=10)
input.pack()
print(input.get())


# Turtle window
# tim = turtle.Turtle()
# tim.write("Some Text", font=("Times New Roman", 30, "bold"))

window.mainloop()



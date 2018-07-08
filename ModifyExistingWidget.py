from tkinter import Tk, Label
root = Tk()

label = Label(root, text='Hello, world')
label.pack()

label.config(foreground='yellow', background='black', text='Updated text!')

root.mainloop()

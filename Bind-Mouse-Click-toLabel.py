from tkinter import Tk, Label
root = Tk()

label = Label(root, text='I am a label. Click me.')
label.pack()

def my_callback():
    print('Label was clicked.')
    
label.bind("<Button-1>", lambda e:my_callback())

root.mainloop()
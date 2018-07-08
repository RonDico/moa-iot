from tkinter import Tk, Label, Y, RIGHT
root = Tk()

label1 = Label(root, text='Yellow!', background='yellow')
label2 = Label(root, text='Orange?', background='orange')

label1.pack(fill=Y, padx=25, ipady=15, side=RIGHT)
label2.pack(fill=Y, padx=25, ipady=15, side=RIGHT)

root.mainloop()

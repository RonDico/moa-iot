from tkinter import Tk, Entry, Button, INSERT
root = Tk()

entry = Entry(root)
entry.pack()

entry.insert(INSERT, 'Hello, world!')

def print_content():
    print(entry.get())
    
button = Button(root, text='Print content', command=print_content)
button.pack()

root.mainloop()


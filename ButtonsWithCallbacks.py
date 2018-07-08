from tkinter import Tk, Button
root = Tk()

exit_button = Button(root, text='Exit Program', command=root.destroy)
exit_button.pack()

def my_callback():
    print("The button was clicked!")
    
print_button = Button(root, text='Click me!', command=my_callback)
print_button.pack()

root.mainloop()

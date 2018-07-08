from tkinter import Tk, Menu
root = Tk()

menu_bar = Menu(root)

file_menu = Menu(root, tearoff=0)

file_menu.add_command(label='Quit', command=root.destroy)
file_menu.add_command(label='Exit', command=root.destroy)
file_menu.add_command(label='End', command=root.destroy)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()


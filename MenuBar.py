from tkinter import Tk, Menu
root = Tk()

main_menu = Menu(root, tearoff=0)

main_menu.add_command(label='Quit', command=root.destroy)

root.config(menu=main_menu)
root.mainloop()

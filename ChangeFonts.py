from tkinter import Tk, Message
root = Tk()

root.geometry("400x150+250+250")

msg = Message(root, text='Hello world!')

msg.config(font=('times', 48, 'italic bold underline'))

msg.pack()

root.mainloop()

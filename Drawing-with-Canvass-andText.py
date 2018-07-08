# canvas_draw.py
from tkinter import Tk, Canvas, Label
root = Tk()

canv = Canvas(root, width=600, height=400)
canv.pack()

# Draw blue line from top left to bottom right with wide dashes
canv.create_line(0, 0, 600, 400, fill='blue', dash=(5, 15))

# Draw green rectangle at (100,50) to (120,55)
canv.create_rectangle(100, 250, 120, 55, fill='green')

# Draw oval(circle) from (20,20) to (40,40)
canv.create_oval(20, 20, 600, 400)


# Draw oval(circle) from (20,20) to (40,40)
canv.create_oval(20, 20, 100, 100, fill='yellow')

labelfont = ('calibri', 40, 'bold')
my_text = Label(root, text='Hello, world!')
my_text.pack()
my_text.place(x=100, y=100)
my_text.config(font=labelfont) 


root.mainloop()

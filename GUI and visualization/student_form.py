from tkinter import *

root = Tk()

Label(root, text="Name").grid(row=0)
Label(root, text="Age").grid(row=1)

Entry(root).grid(row=0, column=1)
Entry(root).grid(row=1, column=1)

Button(root, text="Submit").grid(row=2)

root.mainloop()
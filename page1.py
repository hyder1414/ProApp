from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title("ProApp")
combo = Combobox(root)
combo['values']= ("Java", "Python", "Algorithms", "Data Structure", "Interview", "Events")
combo.current()
combo.grid(column=2, row=4)


root.mainloop()



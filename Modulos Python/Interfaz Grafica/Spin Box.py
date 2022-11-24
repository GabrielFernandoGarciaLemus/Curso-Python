from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x300")

w=Spinbox(root,values =("Python","JavaScript","HTMIL","C++","C#"))
w.pack()

g=Spinbox(root,values =("Fisica I","Programacion I","Metodos y Tecnicas","Tecnologia I"))
g.pack()

root.mainloop()


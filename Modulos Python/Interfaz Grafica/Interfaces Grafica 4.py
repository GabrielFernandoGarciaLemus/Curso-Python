from tkinter import *

root = Tk()
root.title("Prueba 4")
root.iconbitmap("Cerberus.ico")

texto = Text(root)
texto.pack()
texto.config(width=40,height=10,padx=15,pady=15,font=("Curier",20),
             selectbackground="blue")

label=Label(root,text="Escribe algo aqui")
label.pack()
label.config(bg="blue", fg="snow",font=("Curier",15))


root.mainloop()

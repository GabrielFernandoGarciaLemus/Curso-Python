from tkinter import*

root = Tk()

frame  = Frame(root, width=500, height=400 )
frame.pack()

entrada = Entry(frame)
entrada.grid(row=0,column=1,sticky="w",padx=5,pady=5)
entrada.config(justify="center")

entrada2 = Entry(frame)
entrada2.grid(row=1,column=1,sticky="w",padx=5,pady=5)
entrada2.config(justify="center")
entrada2.config(show="*")

label1 = Label(frame,text="Usuario")
label1.config(bg="blue",fg="snow")
label1.grid(row=0,column=0,sticky="w",padx=5,pady=5)

label2 = Label(frame,text="Password")
label2.config(bg="blue",fg="snow")
label2.grid(row=1,column=0,sticky="w",padx=5,pady=5)

boton = Button (frame, text="Ingresar")
boton.grid(row=2,column=1,sticky="w",padx=5,pady=5)


root.mainloop()

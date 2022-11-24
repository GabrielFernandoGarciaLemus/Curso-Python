from tkinter import *

root = Tk()
root.geometry("500x350")
root.iconbitmap("desktop.ico")
root.title("List Box")

productos = Label(root, text = "Productos")
productos.pack()

def agregar():
    listaProductos.insert(END, entrada.get())
def borrar ():
    listaProductos.delete()
    
    
listaProductos = Listbox(root,width=50)
listaProductos.config(font="Curier 12")
listaProductos.pack()

entrada = Entry(root,bd=10)
entrada.pack()


boton = Button(root, text="Agregar",bd=10,command=agregar)
boton.pack()

boton2 = Button(root,text="Eliminar",bd=10,command=borrar)
boton2.pack()


root.mainloop()


from tkinter import* 
from tkinter import messagebox


def salir():
    i = messagebox.askquestion("Salir", "¿Estas seguro que deseas salir? ")
    if i == "yes":
        root.destroy()
        
def acerca():
    messagebox.showinfo("Informacion", "Creado por Gabriel Garcia ")

def licencia():
    messagebox.showinfo("Licencias", "Producto licenciado hasta el 20 de septiembre del 2021")

def error():
    messagebox.showerror("Error Fatal","Tu error fue nacer")
    
def deshacer():
    g = messagebox.askquestion("Advertencia", "¿Estas seguro que deseas deshacer el progreso?")
    if g =="yes":
        root.destroy()
    
root = Tk()

barraMenu = Menu(root)
root.config(menu = barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
archivoMenu.add_command(label = "Nueva Ventana ",command = error)
archivoMenu.add_command(label = "Nuevo Archivo ")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Salir ",command=salir)

archivoEditor = Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label = "Editor ", menu=archivoEditor)
archivoEditor.add_command(label = "Reshacer")
archivoEditor.add_command(label = "Deshacer",command=deshacer)

archivoAyuda = Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label = "Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label = "Acerca de...", command=acerca)
archivoAyuda.add_command(label = "Licencia",command=licencia)



root.mainloop()

from tkinter import* 

root = Tk()

barraMenu = Menu(root)
root.config(menu = barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
archivoMenu.add_command(label = "Nueva Ventana ")
archivoMenu.add_command(label = "Nuevo Archivo ")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Salir ")

archivoEditor = Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label = "Editor ", menu=archivoEditor)
archivoEditor.add_command(label = "Reshacer")
archivoEditor.add_command(label = "Deshacer")

archivoAyuda = Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label = "Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label = "Acerca de...")
archivoAyuda.add_command(label = "Licencia")



root.mainloop()

from tkinter import *

root = Tk()


root.title("Prueba de Interfaz Grafica")
root.config(width=400, height=300 )



label = Label(root, text= "Hola Mundo")
label.place(x=200, y=50)
label.config(bg="green",fg="snow", font=("Curier", 20))

label = Label(root, text= "Bienvenidos")
label.place(x=25,y=50)
label.config(bg="red",fg="snow", font=("Curier",20))


root.mainloop()
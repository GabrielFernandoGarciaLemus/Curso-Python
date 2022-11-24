from tkinter import *

root = Tk()
root.title("Radio Button")
root.resizable(1,1)
root.iconbitmap("desktop.ico")


opciones = IntVar()
def mostrar():
    if opciones.get()==1:
        label2.config(text="Has elegido la opcion Masculino",font="Curier 15",bg="black",fg="white")
        
    elif opciones.get()==2:
        label2.config(text="Has elegido la opcion Femenino",font="Curier 15",bg="pink",fg="skyblue")

    elif opciones.get()==3:
        label2.config(text="Has elegido la opcion Unico y Diferente",font="Curier 15",bg="purple",fg="green")
        


label1 = Label(root,text="Elige un genero")
label1.config(bg="blue",fg="snow",font="Curier 20")
label1.pack()


Radiobutton(root,text="Maculino",variable=opciones,value=1,command=mostrar,font="Curier 20").pack()
Radiobutton(root,text="Femenino",variable=opciones,value=2,command=mostrar,font="Curier 20").pack()
Radiobutton(root,text="No binario",variable=opciones,value=3,command=mostrar,font="Curier 20").pack()


label2=Label(root)
label2.pack()






root.mainloop()
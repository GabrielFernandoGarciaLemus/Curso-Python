from tkinter import *


def  sumar():
    resultado.set(int(val1.get()) +int(val2.get()))
    
def  restar():
    resultado.set(int(val1.get()) - int(val2.get()))
    
def  multiplicar():
    resultado.set(int(val1.get()) * int(val2.get()))

def  dividir():
    resultado.set(int(val1.get()) / int(val2.get()))

root = Tk()
root.title("Mini Calculadora")
root.iconbitmap("calculator.ico")
root.geometry("400x300")


val1 = StringVar()
val2 = StringVar()
resultado = StringVar()


frame = Frame(root,width=1000,height=600)
frame.pack()


entrada1 = Entry(frame)
entrada1.config(bd=10,font="Curier 20", textvariable=val1)
entrada1.pack()


entrada2 = Entry(frame)
entrada2.config(bd=10,font="Curier 20", textvariable = val2)
entrada2.pack()

entrada3 = Entry(frame)
entrada3.config(bd=10,font="Curier 20",state="disable", textvariable= resultado)
entrada3.pack()


boton1= Button(frame,text= "Sumar")
boton1.config(bd=5,font="Curier 10",command=sumar)
boton1.pack()

boton2= Button(frame,text= "Restar")
boton2.config(bd=5,font="Curier 10",command=restar)
boton2.pack()


boton3= Button(frame,text= "Multiplicar")
boton3.config(bd=5,font="Curier 10",command=multiplicar)
boton3.pack()


boton4= Button(frame,text= "Dividir")
boton4.config(bd=5,font="Curier 10",command=dividir)
boton4.pack()

root.mainloop() 
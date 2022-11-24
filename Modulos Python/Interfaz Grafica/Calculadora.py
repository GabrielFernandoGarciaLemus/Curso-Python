from tkinter import*


g = 0

def click(valor):
    global g
    Entrada.insert(g,valor)
    g += 1
    
def borrar():
    Entrada.delete(0,END)
    g = 0
    
def operaciones():
    operacion = Entrada.get()
    resultado = eval(operacion)
    Entrada.delete(0,END)
    Entrada.insert(0, resultado)
    g = 0
      
root = Tk()
root.title("Mi Calculadora")
root.iconbitmap("calculator.ico")

#Entrada
Entrada = Entry(root,font = ("Curier 25"))
Entrada.grid(row= 0, column = 0, columnspan = 4, padx = 10, pady = 10)

#Botones
boton1 = Button(root, text= "1", width=10, height=5, bd=5, command = lambda:click(1))
boton2 = Button(root, text= "2", width=10, height=5, bd=5, command = lambda:click(2))
boton3 = Button(root, text= "3", width=10, height=5, bd=5, command = lambda:click(3))
boton4 = Button(root, text= "4", width=10, height=5, bd=5, command = lambda:click(4))
boton5 = Button(root, text= "5", width=10, height=5, bd=5, command = lambda:click(5))
boton6 = Button(root, text= "6", width=10, height=5, bd=5, command = lambda:click(6))
boton7 = Button(root, text= "7", width=10, height=5, bd=5, command = lambda:click(7))
boton8 = Button(root, text= "8", width=10, height=5, bd=5, command = lambda:click(8))
boton9 = Button(root, text= "9", width=10, height=5, bd=5, command = lambda:click(9))
boton0 = Button(root, text= "0", width=25, height=5, bd=5, command = lambda:click(0))

boton_borrar = Button(root, text= "DEL", width=10, height=5, bd=5, command = lambda:borrar())
boton_parentesis1 = Button(root, text= "(", width=10, height=5, bd=5, command = lambda:click("("))
boton_parentesis2 = Button(root, text= ")", width=10, height=5, bd=5, command = lambda:click(")"))
boton_punto = Button(root, text= ".", width=10, height=5, bd=5, command = lambda:click("."))

boton_suma = Button(root, text= "SUM", width=10, height=5, bd=5, command = lambda:click("+"))
boton_resta = Button(root, text= "REST", width=10, height=5, bd=5, command = lambda:click("-"))
boton_multi = Button(root, text= "MULT", width=10, height=5, bd=5, command = lambda:click("*"))
boton_div = Button(root, text= "DIV", width=10, height=5, bd=5, command = lambda:click("/"))
boton_igual = Button(root, text= "=", width=10, height=5, bd=5, command = lambda:operaciones())

#Colocar Botones

boton_borrar.grid(row = 1,column = 0, padx= 5, pady= 5 )
boton_parentesis1.grid(row = 1,column = 1, padx= 5, pady= 5 )
boton_parentesis2.grid(row = 1,column = 2, padx= 5, pady= 5 )
boton_div.grid(row = 1,column = 3, padx= 5, pady= 5)

boton7.grid(row = 2,column = 0, padx= 5, pady= 5 )
boton8.grid(row = 2,column = 1, padx= 5, pady= 5 )
boton9.grid(row = 2,column = 2, padx= 5, pady= 5 )
boton_multi.grid(row = 2,column = 3, padx= 5, pady= 5)

boton4.grid(row = 3,column = 0, padx= 5, pady= 5 )
boton5.grid(row = 3,column = 1, padx= 5, pady= 5 )
boton6.grid(row = 3,column = 2, padx= 5, pady= 5 )
boton_suma.grid(row = 3,column = 3, padx= 5, pady= 5)

boton1.grid(row = 4,column = 0, padx= 5, pady= 5 )
boton2.grid(row = 4,column = 1, padx= 5, pady= 5 )
boton3.grid(row = 4,column = 2, padx= 5, pady= 5 )
boton_resta.grid(row = 4,column = 3, padx= 5, pady= 5)


boton0.grid(row = 5,column = 0,columnspan = 2, padx= 5, pady= 5 )
boton_punto.grid(row = 5,column = 2, padx= 5, pady= 5 )
boton_igual.grid(row = 5,column = 3, padx= 5, pady= 5 )





root.mainloop()

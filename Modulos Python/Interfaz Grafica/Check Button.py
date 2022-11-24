from tkinter import *

root = Tk()
root.geometry("660x300")
root.title("Check Button")
root.config(bd=20,bg="goldenrod3")
root.iconbitmap("desktop.ico")

def orden():
    lista = "Hamburguesa:  "
    if (queso.get()):
        lista +=" con queso" 
        
    if (lechuga.get()):
        lista +=" y con lechuga " 
    
    if (tocino.get()):
        lista +=" y con tocino " 
        
    if (res.get()):
        lista +=" y con carne de Res " 

    if (pollo.get()):
        lista +=" y con carne de Pollo " 

    imprimir.config(text=lista)
        
    

queso = IntVar()
lechuga = IntVar()
tocino = IntVar()
res = IntVar()
pollo = IntVar() 

imagen = PhotoImage(file="hamburguesa.gif")
Label(root,image = imagen).pack(side = LEFT)

frame = Frame(root)
frame.pack(side= RIGHT)
frame.config(bg="goldenrod3")


Label(frame, text = "Como deseas tu hamburguesa:", bg="goldenrod3", font= "Curier 15" ).pack(anchor="w")

Checkbutton(frame,text="Con Queso",variable = queso, onvalue=1, offvalue=0, bg="goldenrod3", font= "Curier 10", command =orden ).pack(anchor="w")
Checkbutton(frame,text="Con Lechuga",variable = lechuga, onvalue=1, offvalue=0,bg="goldenrod3", font= "Curier 10" , command =orden ).pack(anchor="w")
Checkbutton(frame,text="Con Tocino",variable = tocino, onvalue=1, offvalue=0, bg="goldenrod3", font= "Curier 10" , command =orden ).pack(anchor="w")
Checkbutton(frame,text="Con Carne de Res",variable = res, onvalue=1, offvalue=0, bg="goldenrod3", font= "Curier 10" , command =orden).pack(anchor="w")
Checkbutton(frame,text="Con Carne de Pollo",variable = pollo, onvalue=1, offvalue=0, bg="goldenrod3", font= "Curier 10", command =orden  ).pack(anchor="w")

imprimir = Label(frame, bg= "goldenrod3")
imprimir.pack()
imprimir.config(font="Curier 10")

root.mainloop()

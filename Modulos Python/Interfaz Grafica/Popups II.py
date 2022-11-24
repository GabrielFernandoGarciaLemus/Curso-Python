from tkinter import*
from tkinter import filedialog

root = Tk()


def abrir():
    archivo = filedialog.askopenfilename(title = "Abrir",initialdir = "Descargas",filetypes=(("Documento de Texto","*.txt"),("Documento Excel","*.xlsx")))
    print(archivo)
    
Button(root,text ="Archivo",command=abrir).pack()




root.mainloop()
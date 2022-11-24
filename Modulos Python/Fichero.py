from io import open

fichero = open("archivo.txt","a")
fichero.write("\n Este es el metodo Append")
fichero.close()
print(fichero)

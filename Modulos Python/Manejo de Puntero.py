from io import open

fichero = open("Prueba.txt", "r+")

print(fichero.readlines())

fichero.close()
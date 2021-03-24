from libro import Libro
from autor import Autor
def get_list():
    dic = {}
    f = open("alo.txt", mode="rt", encoding="utf-8")
    """for linea in f:
        if linea[f] =! None:
            diccionario.append(f)
    return diccionario"""
    #print("he leído: " + linea)
    #f.readlines()
        
#-----------------------------------------
a = get_list()
print("La palabra con mayor tamaño sera: ", a)
l1 = Libro(autor = Autor(id_autor = "1", nombre = "Alex", apellidos = "Cebolla"), titulo = "quijote", anyo = "anyo")
l2 = Libro(autor = Autor(id_autor = "2", nombre = "Carmen", apellidos = "Pardo"), titulo = "hola", anyo = "anyo")
l3 = Libro(autor = Autor(id_autor = "3", nombre = "Luis", apellidos = "Cebolla"), titulo = "adios", anyo = "anyo")

print(l1)

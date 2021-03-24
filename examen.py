from libro import Libro
from autor import Autor
def get_list():
    dic = {}
    f = open("alo.txt", mode="rt", encoding="utf-8")
    """for linea in f:
        if linea[f] =! None:
            diccionario.append(f)
    return diccionario"""
  
print  #print("he leído: " + linea)
    #f.readlines()
        
#-----------------------------------------
a = get_list()
("La palabra con mayor tamaño sera: ", a)
l1 = Libro(autor = Autor(id_autor = "1", nombre = "Alex", apellido = "Cebolla"), titulo = "quijote", anyo = "2010")
l2 = Libro(autor = Autor(id_autor = "2", nombre = "Carmen", apellido = "Pardo"), titulo = "hola", anyo = "1980")
l3 = Libro(autor = Autor(id_autor = "3", nombre = "Luis", apellido = "Cebolla"), titulo = "adios", anyo = "2011")
lista = list()
lista.append(l1)
lista.append(l2)
lista.append(l3)
print(lista)

def mas_antiguos(l, year):
    for i in l:
        if l[i].anyo > "1900" and l[i].anyo < "2021":
            return l[i].titulo
        else:
            raise ValueError("El anyo no es valido")


b = mas_antiguos(lista, "2010")
print(b)

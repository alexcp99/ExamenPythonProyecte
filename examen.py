from libro import Libro
from autor import Autor
def get_list():
    """dic = {}
    f = open("alo.txt", mode="rt", encoding="utf-8")
    for linea in f:
            dic.append(linea[f])
    return dic"""

        
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
for i in lista:
    print(lista[i])

def mas_antiguos(l, year):
    lista = list()
    for i in l:
        if l[i].anyo > "1900" and l[i].anyo < "2021":
            l[i].get_titulo()
        else:
            raise ValueError("El anyo no es valido")
    return l


b = mas_antiguos(lista, "2010")
print(b)

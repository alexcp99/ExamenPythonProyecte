import unittest
from examen import *

class Pruebas(unittest.TestCase):
    """
    Archivo test.py, donde vamos a hacer un control de errores
    y una serie de comprobaciones

    """

    def test_mas_antiguos(self):
        l2 = Libro(autor = Autor(id_autor = "2", nombre = "Carmen", apellido = "Pardo"), titulo = "hola", anyo = "1980")
        self.assertEqual(l2.get_titulo, "hola")

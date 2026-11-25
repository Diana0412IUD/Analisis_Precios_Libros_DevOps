
import unittest
import os

class TestPaginaWeb(unittest.TestCase):

    def setUp(self):
        self.ruta = os.path.join("docs", "index.html")

        with open(self.ruta, encoding="utf-8") as archivo:
            self.contenido = archivo.read()

    def test_pagina_web_existe(self):
        self.assertTrue(os.path.exists(self.ruta))

    def test_titulo_pagina(self):
        self.assertIn("Análisis de precios de libros", self.contenido)

    def test_resultados_del_analisis(self):
        self.assertIn("£38.05", self.contenido)
        self.assertIn("£13.99", self.contenido)
        self.assertIn("£57.25", self.contenido)

    def test_funcion_interactiva(self):
        self.assertIn("mostrarDetalles()", self.contenido)
        self.assertIn("Ver detalles del proyecto", self.contenido)

if __name__ == "__main__":
    unittest.main()

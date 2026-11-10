
import unittest
import csv
import os

class TestDatosLibros(unittest.TestCase):

    def test_archivo_csv_existe(self):
        self.assertTrue(os.path.exists("libros_scraping.csv"))

    def test_csv_contiene_datos(self):
        with open("libros_scraping.csv", encoding="utf-8-sig") as archivo:
            datos = list(csv.reader(archivo))

        self.assertGreater(len(datos), 1)
        self.assertGreaterEqual(len(datos[0]), 2)

    def test_registros_completos(self):
        with open("libros_scraping.csv", encoding="utf-8-sig") as archivo:
            datos = list(csv.reader(archivo))

        for fila in datos[1:]:
            self.assertGreaterEqual(len(fila), 2)
            self.assertTrue(fila[0].strip())
            self.assertTrue(fila[1].strip())

if __name__ == "__main__":
    unittest.main()

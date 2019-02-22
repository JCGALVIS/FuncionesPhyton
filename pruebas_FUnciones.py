import unittest
import Funciones as f

class pruebas(unittest.TestCase):

    def test_es_vocal(self):
        self.assertEqual(f.es_vocal('b'), False)
        self.assertEqual(f.es_vocal('A'), True)
        self.assertEqual(f.es_vocal('e'), True)
        self.assertEqual(f.es_vocal('i'), True)
        self.assertEqual(f.es_vocal('o'), True)
        self.assertEqual(f.es_vocal('u'), True)
        self.assertEqual(f.es_vocal('bfsf'), False)
        self.assertEqual(f.es_vocal('aeiou'), False)

    def test_area_sombreada(self):
        self.assertAlmostEqual(f.area_sombreada(5), -34.29203673205103)
        self.assertAlmostEqual(f.area_sombreada(2),  -1.7168146928204138)

if __name__ == 'main':
    unittest.main()



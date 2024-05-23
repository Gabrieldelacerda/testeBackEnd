import unittest
from app import calcular_combinacoes

class TestPontuacoes(unittest.TestCase):
    def test_combinacoes_validas(self):
        self.assertEqual(calcular_combinacoes("3x15"), 4)
        self.assertEqual(calcular_combinacoes("0x0"), 1)
        self.assertEqual(calcular_combinacoes("6x6"), 4)

    def test_combinacoes_invalidas(self):
        self.assertEqual(calcular_combinacoes("8x5"), 0)
        self.assertEqual(calcular_combinacoes("1x1"), 0)

if __name__ == '__main__':
    unittest.main()

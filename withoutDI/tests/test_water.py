import unittest
from withoutDI.water import Water

class TestWater(unittest.TestCase):
    def test_water(self):
        w:Water = Water(temperature=50, purity=0.9)
        self.assertEqual(w.temperature, 50)
        self.assertEqual(w.purity, 0.9)


if __name__ == '__main__':
    unittest.main()

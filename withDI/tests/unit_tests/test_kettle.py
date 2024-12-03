import unittest
from withDI.kettle import Kettle
from withDI.water import Water


class TestKettle(unittest.TestCase):
    def test_default_kettle(self):
        w: Water = Water(temperature=20, purity=0.6)
        self.assertEqual(w.temperature, 20)
        k :Kettle = Kettle()
        k.heat_water(w)
        self.assertEqual(w.temperature, 95)


    def test_custom_kettle(self):
        w: Water = Water(temperature=20, purity=0.6)
        self.assertEqual(w.temperature, 20)
        k :Kettle = Kettle(88)
        k.heat_water(w)
        self.assertEqual(w.temperature, 88)


if __name__ == '__main__':
    unittest.main()

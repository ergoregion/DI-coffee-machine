import unittest
from withoutDI.coffee import Coffee

class TestCoffee(unittest.TestCase):
    def test_water(self):
        c:Coffee = Coffee(temperature=50, strength= 3.4, taste=2.3)
        self.assertEqual(c.temperature, 50)
        self.assertEqual(c.strength, 3.4)
        self.assertEqual(c.taste, 2.3)


if __name__ == '__main__':
    unittest.main()
import unittest
from withoutDI.coffee_process import CoffeeProcess
from withoutDI.coffee import Coffee


class TestCoffeeProces(unittest.TestCase):
    def test_coffee_process(self):
        coffee_process: CoffeeProcess = CoffeeProcess()
        coffee: Coffee = coffee_process.make_coffee()

        self.assertEqual(coffee.temperature, 92)
        self.assertEqual(coffee.strength, 5.2)
        self.assertEqual(coffee.taste, 4.888)


if __name__ == '__main__':
    unittest.main()

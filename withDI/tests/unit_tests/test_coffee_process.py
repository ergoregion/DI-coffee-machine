import unittest
from withDI.coffee_process import CoffeeProcess, Coffee
from withDI.iWaterProvider import iWaterProvider
from withDI.water import Water


class TestingWaterProvider(iWaterProvider):

    def get_water(self) -> Water:
        return Water(
            temperature=98,
            purity=0.94
        )


class TestCoffeeProces(unittest.TestCase):
    def test_coffee_process(self):
        coffee_process: CoffeeProcess = CoffeeProcess(TestingWaterProvider())
        coffee: Coffee = coffee_process.make_coffee()

        self.assertEqual(coffee.temperature, 92)
        self.assertEqual(coffee.strength, 5.2)
        self.assertEqual(coffee.taste, 4.888)



if __name__ == '__main__':
    unittest.main()

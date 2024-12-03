import unittest
from withDI.coffee_process import CoffeeProcess
from withDI.iWaterProvider import iWaterProvider
from withDI.coffee import Coffee
from withDI.tap import Tap
from withDI.ketle_heated_water_provider import KettleHeatedWaterProvider


class TestCoffeeProces(unittest.TestCase):
    def test_coffee_process(self):
        cold_water_provider: iWaterProvider = Tap()
        hot_water_provider: iWaterProvider = KettleHeatedWaterProvider(cold_water_provider)
        coffee_process: CoffeeProcess = CoffeeProcess(hot_water_provider)
        coffee: Coffee = coffee_process.make_coffee()

        self.assertEqual(coffee.temperature, 92)
        self.assertEqual(coffee.strength, 5.2)
        self.assertEqual(coffee.taste, 4.888)


if __name__ == '__main__':
    unittest.main()

import unittest
from withDI.coffee_process import CoffeeProcess, Coffee
from withDI.iWaterProvider import iWaterProvider
from withDI.water import Water


class TestingColdWaterProvider(iWaterProvider):

    def get_water(self) -> Water:
        return Water(
            temperature=55,
            purity=0.9
        )


class TestCoffeeProcesWithColdWater(unittest.TestCase):

    def test_coffee_process_with_cold_water(self):
        coffee_process: CoffeeProcess = CoffeeProcess(TestingColdWaterProvider())

        with self.assertRaises(Exception):
            coffee_process.make_coffee()



if __name__ == '__main__':
    unittest.main()

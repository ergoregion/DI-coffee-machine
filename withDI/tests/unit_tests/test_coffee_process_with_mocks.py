import unittest
from withDI.coffee_process import CoffeeProcess, Coffee
from withDI.iWaterProvider import iWaterProvider
from withDI.water import Water

from unittest.mock import Mock

class TestCoffeeProcesMocks(unittest.TestCase):
    def test_coffee_process(self):

        mock_water_provider = iWaterProvider()
        mock_water_provider.get_water = Mock(return_value=Water(temperature=98,purity=0.94))

        coffee_process: CoffeeProcess = CoffeeProcess(mock_water_provider)
        coffee: Coffee = coffee_process.make_coffee()

        self.assertEqual(coffee.temperature, 92)
        self.assertEqual(coffee.strength, 5.2)
        self.assertEqual(coffee.taste, 4.888)

    def test_coffee_process_cold_water(self):

        mock_water_provider = iWaterProvider()
        mock_water_provider.get_water = Mock(return_value=Water(temperature=55,purity=0.90))

        coffee_process: CoffeeProcess = CoffeeProcess(mock_water_provider)

        with self.assertRaises(Exception):
            coffee_process.make_coffee()

    def test_coffee_process_only_needs_one_water(self):

        mock_water_provider = iWaterProvider()
        mock_water_provider.get_water = Mock(return_value=Water(temperature=98,purity=0.94))

        coffee_process: CoffeeProcess = CoffeeProcess(mock_water_provider)
        coffee: Coffee = coffee_process.make_coffee()

        mock_water_provider.get_water.assert_called_once()

if __name__ == '__main__':
    unittest.main()

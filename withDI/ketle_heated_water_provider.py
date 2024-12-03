from .kettle import Kettle
from .iWaterProvider import iWaterProvider
from .water import Water


class KettleHeatedWaterProvider(iWaterProvider):
    _kettle = Kettle(98)
    _water_provider: iWaterProvider

    def __init__(self, water_provider: iWaterProvider):
        self._water_provider = water_provider

    def get_water(self) -> Water:
        w: Water = self._water_provider.get_water()
        self._kettle.heat_water(w)
        return w

from .water import Water
from .iWaterProvider import iWaterProvider
from .coffee import Coffee


class CoffeeProcess:


    def __init__(self, water_provider: iWaterProvider):
        self._water_provider: iWaterProvider = water_provider

    def make_coffee(self):

        w: Water = self._water_provider.get_water()
        return self._brew_coffee(w)

    def _brew_coffee(self, w: Water) -> Coffee:

        if w.temperature < 80:
            raise Exception("Your water is too cold")

        _strength: float = 5.2
        return Coffee(temperature=w.temperature - 6,
                      strength=_strength,
                      taste=w.purity * _strength)

from .water import Water
from .tap import Tap
from .kettle import Kettle
from .coffee import Coffee


class CoffeeProcess:

    _tap = Tap()
    _kettle = Kettle(98)

    def make_coffee(self):

        w: Water = self._tap.get_water()

        self._kettle.heat_water(w)

        return self._brew_coffee(w)

    def _brew_coffee(self, w: Water) -> Coffee:

        if w.temperature < 80:
            raise Exception("Your water is too cold")

        _strength: float = 5.2
        return Coffee(temperature=w.temperature - 6,
                      strength=_strength,
                      taste=w.purity * _strength)

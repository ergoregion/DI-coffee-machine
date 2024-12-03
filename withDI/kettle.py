from .water import Water


class Kettle:
    _target_temperature = 95

    def __init__(self, target_temperature=95):
        self._target_temperature = target_temperature

    def heat_water(self, input_water: Water) -> None:
        input_water.temperature = self._target_temperature


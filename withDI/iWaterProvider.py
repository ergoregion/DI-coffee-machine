from .water import Water


class iWaterProvider:
    def get_water(self) -> Water:
        raise NotImplementedError
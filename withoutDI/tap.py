from .water import Water


class Tap:
    def get_water(self) -> Water:
        # This could be elaborate calculations, loading large files, or acquiring data from a remote source
        # Anything with cost associated

        return Water(temperature=16, purity=0.94)



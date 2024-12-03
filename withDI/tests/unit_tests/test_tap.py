import unittest
from withDI.tap import Tap

class TestTap(unittest.TestCase):
    def test_tap(self):
        tap: Tap = Tap()
        w = tap.get_water()
        self.assertEqual(w.temperature, 16)
        self.assertEqual(w.purity, 0.94)


if __name__ == '__main__':
    unittest.main()

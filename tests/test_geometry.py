import unittest
import numpy as np
from scanner.detection import order_points


class GeometryTests(unittest.TestCase):
    def test_order_points(self):
        unordered = np.array([[90, 80], [10, 10], [10, 80], [90, 10]], dtype=np.float32)
        ordered = order_points(unordered)
        expected = np.array([[10, 10], [90, 10], [90, 80], [10, 80]], dtype=np.float32)
        np.testing.assert_array_equal(ordered, expected)


if __name__ == "__main__":
    unittest.main()

from random import randrange
import unittest

from main import DataCapture


class StatsTest(unittest.TestCase):
    def test_less(self):
        cap = DataCapture()
        for i in range(0, 1000):
            cap.add(i)
        stats = cap.build_stats()
        result = stats.less(98)
        self.assertEqual(result, 98)

    def test_less_random(self):
        cap = DataCapture()
        for _ in range(100):
            cap.add(randrange(100))
        for _ in range(800):
            cap.add(randrange(100, 150))
        for _ in range(100):
            cap.add(randrange(100))
        stats = cap.build_stats()
        result = stats.less(100)
        self.assertEqual(result, 200)

    def test_greater(self):
        cap = DataCapture()
        for i in range(0, 100):
            cap.add(i)
        stats = cap.build_stats()
        result = stats.greater(20)
        self.assertEqual(result, 79)

    def test_between(self):
        cap = DataCapture()
        for i in range(0, 100):
            cap.add(i)
        stats = cap.build_stats()
        result = stats.between(19, 32)
        self.assertEqual(result, 14)

    def test_between_random(self):
        cap = DataCapture()
        for _ in range(100):
            cap.add(randrange(100))
        for _ in range(800):
            cap.add(randrange(100, 151))
        for _ in range(100):
            cap.add(randrange(151, 1000))
        stats = cap.build_stats()
        result = stats.between(100, 150)
        self.assertEqual(result, 800)


if __name__ == "__main__":
    unittest.main()

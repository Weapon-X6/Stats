from random import randrange
import unittest

from main import DataCapture


class StatsTest(unittest.TestCase):
    def test_add(self):
        cap = DataCapture()

        for n in (10, 9, 45, 7, 2, 948):
            cap.add(n)

        self.assertEqual(cap.data, [10, 9, 45, 7, 2, 948])

    def test_add_invalid_value(self):
        cap = DataCapture()

        with self.assertRaises(ValueError):
            cap.add(-5)
        with self.assertRaises(ValueError):
            cap.add(0)
        with self.assertRaises(ValueError):
            cap.add(2023)

    def test_add_invalid_type(self):
        cap = DataCapture()

        with self.assertRaises(TypeError):
            cap.add("45")
        with self.assertRaises(TypeError):
            cap.add(False)
        with self.assertRaises(TypeError):
            cap.add(1.0)

    def test_less(self):
        cap = DataCapture()

        for _ in range(100):
            cap.add(randrange(1, 100))
        for _ in range(800):
            cap.add(randrange(100, 150))
        for _ in range(100):
            cap.add(randrange(1, 100))
        stats = cap.build_stats()

        self.assertEqual(stats.less(100), 200)
        self.assertEqual(stats.less(1), 0)
        self.assertEqual(stats.less(0), 0)
        self.assertEqual(stats.less(1000), 1000)

    def test_less_invalid_type(self):
        cap = DataCapture()
        cap.add(32)
        cap.add(19)
        stats = cap.build_stats()

        with self.assertRaises(TypeError):
            stats.less("2")
        with self.assertRaises(TypeError):
            stats.less(2.0)
        with self.assertRaises(TypeError):
            stats.less(False)

    def test_less_invalid_value(self):
        cap = DataCapture()
        cap.add(32)
        cap.add(19)
        stats = cap.build_stats()

        with self.assertRaises(ValueError):
            stats.less(-1)
        with self.assertRaises(ValueError):
            stats.less(5000)

    def test_greater(self):
        cap = DataCapture()

        for i in range(1, 101):
            cap.add(i)
        stats = cap.build_stats()

        self.assertEqual(stats.greater(20), 80)
        self.assertEqual(stats.greater(0), 100)
        self.assertEqual(stats.greater(100), 0)

    def test_greater_invalid_type(self):
        cap = DataCapture()
        cap.add(34)
        cap.add(21)
        stats = cap.build_stats()

        with self.assertRaises(TypeError):
            stats.greater("2")
        with self.assertRaises(TypeError):
            stats.greater(2.0)
        with self.assertRaises(TypeError):
            stats.greater(False)

    def test_greater_invalid_value(self):
        cap = DataCapture()
        cap.add(34)
        cap.add(21)
        stats = cap.build_stats()

        with self.assertRaises(ValueError):
            stats.greater(-1)
        with self.assertRaises(ValueError):
            stats.greater(5000)

    def test_between(self):
        cap = DataCapture()
        for _ in range(100):
            cap.add(randrange(1, 100))
        for _ in range(800):
            cap.add(randrange(100, 151))
        for _ in range(100):
            cap.add(randrange(151, 999))
        stats = cap.build_stats()

        self.assertEqual(stats.between(100, 150), 800)
        self.assertEqual(stats.between(0, 99), 100)

    def test_between_invalid_type(self):
        cap = DataCapture()
        cap.add(32)
        cap.add(19)
        stats = cap.build_stats()

        with self.assertRaises(TypeError):
            stats.between(1.0, 32)
        with self.assertRaises(TypeError):
            stats.between(False, 32)
        with self.assertRaises(TypeError):
            stats.between("1", 32)
        with self.assertRaises(TypeError):
            stats.between(0, 1.0)
        with self.assertRaises(TypeError):
            stats.between(40, False)
        with self.assertRaises(TypeError):
            stats.between(19, "32")

    def test_between_invalid_value(self):
        cap = DataCapture()
        cap.add(35)
        cap.add(21)
        stats = cap.build_stats()

        with self.assertRaises(ValueError):
            stats.between(-1, 35)
        with self.assertRaises(ValueError):
            stats.between(1000, 3500)
        with self.assertRaises(ValueError):
            stats.between(0, 3500)
        with self.assertRaises(ValueError):
            stats.between(0, -50)


if __name__ == "__main__":
    unittest.main()

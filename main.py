from collections import defaultdict


class Stats:
    """
    class that handles stats from a numeric list
    """

    def __init__(self, data: list) -> None:
        self.data: dict = defaultdict(int)
        for k in data:
            self.data[k] += 1

    def less(self, number: int) -> int:
        """Return the amount of numbers less than number in the instance list"""
        return sum(self.data.get(k) for k in self.data if k < int(number))

    def greater(self, number: int) -> int:
        """Return the amount of number greater than number in the instance list"""
        return sum(self.data.get(k) for k in self.data if k > int(number))

    def between(self, start: int, end: int) -> int:
        """Return the amount of number in greater or equal than start
        and less or equal than end in the instance list"""
        return sum(self.data.get(k) for k in self.data if int(start) <= k <= int(end))


class DataCapture:
    """
    Class that capture values on a iterable for further processing
    """

    def __init__(self) -> None:
        self.data: list = []

    def add(self, number: int) -> None:
        """Add a number to the instance list"""
        self.data.append(number)

    def build_stats(self) -> Stats:
        """Build a Stats object using the current values on the instance list"""
        return Stats(self.data)

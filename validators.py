"""
Module to validate data
"""


def validate_number_in_range(number: int, start: int, end: int):
    """validates that number is an int & in the valid range"""
    msg = f"value needs to be in the range: {start}-{end}"

    if not type(number) is int:
        raise TypeError(msg)
    if not start <= number <= end:
        raise ValueError(msg)

import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
     -> list[int | float]:
    """function to calculate bmi based of \
        the height and weight given

    Args:
        height (list[int  |  float]): height in m
        weight (list[int  |  float]): weight in kg
    Returns:
        list[int | float]: list of calculated bmi
    """
    assert type(height) is list, "height is not a list"
    assert type(weight) is list, "weight is not a list"

    arr_height = np.array(height)
    arr_weight = np.array(weight)

    assert len(arr_height) == len(arr_weight), \
        "arrays must have the same length"
    assert all(np.issubdtype(x, np.number) for x in arr_height), \
        "invalid height"
    assert all(np.issubdtype(x, np.number) for x in arr_weight), \
        "invalid weight"
    assert all(arr_height > 0) is True, "array should be positive, \
        height should be more than 0 to be divisible"
    assert all(arr_weight >= 0) is True, "array should be positive"

    return list(arr_weight / np.square(arr_height))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """funtion that return list[bool]
true if x bigger than limit, false if not"""
    return [x > limit for x in bmi]

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """function that takes a 2D array, prints its shape,
and returns the array as a list"""
    assert type(family) is list, "family is not a list"
    assert type(start) is int and type(end) is int, "not an int"
    n_family = np.asarray(family)
    assert n_family.ndim == 2, "family not 2D"
    print("My shape is :", n_family.shape)
    new_shape = n_family[start:end]
    print("My new shape is :", new_shape.shape)
    return new_shape.tolist()

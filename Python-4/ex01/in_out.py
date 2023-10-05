def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    """outer func. return inner func"""
    count = 0

    def inner() -> float:
        """closure function: applies the given function to the
stored value. return result of the func and update stored value"""
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count

    return inner

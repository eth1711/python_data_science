def mean(num, len_n):
    """mean of list of data,function
calculate and return mean of given list"""
    return sum(num) / len_n


def median(num, len_n):
    """median of list of data, function
calculate and return median of given list"""
    mid = len_n // 2
    if len_n % 2 == 0:
        return (num[mid - 1] + num[mid]) / 2
    else:
        return num[mid]


def quartile(num, len_n):
    """quartile of list of data, function that calculates
and returns the quartiles(tuple of the 25% and 75%) of given lsit"""
    q_25 = round(0.25 * (len_n + 1)) - 1
    q_75 = round(0.75 * (len_n + 1)) - 1
    return float(num[q_25]), float(num[q_75])


def variance(num, len_n):
    """variance of list of data, function that calculates
and returns the variance of given list"""
    return sum(pow(x-mean(num, len_n), 2) for x in num) / len_n


def ft_statistics(*args, **kwargs):
    """ft_statistivs(variable num, keyword arg with the
stat to calculate), function calculate and prints
different statistics of the given data"""
    assert all([isinstance(x, (int, float)) for x in args]), \
        "must be either int or float"
    args = sorted(list(args))
    len_arg = len(args)
    for x in kwargs:
        if not args:
            print("ERROR")
        elif kwargs[x] == 'mean':
            print('mean :', mean(args, len_arg))
        elif kwargs[x] == 'median':
            print('median :', median(args, len_arg))
        elif kwargs[x] == 'quartile':
            print('quartile :', quartile(args, len_arg))
        elif kwargs[x] == 'var':
            print('var :', variance(args, len_arg))
        elif kwargs[x] == 'std':
            print('std :', variance(args, len_arg) ** 0.5)

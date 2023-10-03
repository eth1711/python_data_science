def ft_filter(func, iter):
    """function that basically filters an item.
Func can contain soemthing or be None. Funtion should
return an iterator of those items for which function(item) is true.
if function is None, return the items that are true.This function uses
list comprehension, which needs to be used to fulfill part2 """
    if func is None:
        n_iter = [x for x in iter if x]
    else:
        n_iter = [x for x in iter if func(x)]
    return (n_iter)

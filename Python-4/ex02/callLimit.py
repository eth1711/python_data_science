def callLimit(limit: int):
    """outer function used to store count"""
    count = 0

    def callLimiter(function):
        """decorator"""
        def limit_function(*args, **kwds):
            """wrapper function that wraps the function
            and adds addtional funcs to it"""
            nonlocal count
            if count < limit:
                count += 1
                function(*args, **kwds)
            else:
                print("Error:", function, "call too many times")
        return limit_function
    return callLimiter

def memoize(func):
    cache = {}  

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func



@memoize
def expensive_function(x, y):
    return x + y

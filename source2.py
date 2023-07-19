def my_logger(func):
    import logging
    print(func.__name__)
    logging.basicConfig(filename=f"{func.__name__}.log", level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@my_logger

def func(a, b):
    return "value"

func(4,"Hello")

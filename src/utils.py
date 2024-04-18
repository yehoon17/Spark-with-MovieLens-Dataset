import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        is_time = kwargs.pop('is_timer', False)
        if is_time:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        else:
            result = func(*args, **kwargs)
        return result
    return wrapper


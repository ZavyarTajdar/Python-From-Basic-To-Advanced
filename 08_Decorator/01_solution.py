import time

def time_calculation(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@time_calculation
def example_function(n):
    time.sleep(n)

example_function(10)

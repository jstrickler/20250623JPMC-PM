from functools import wraps
import logging

logging.basicConfig(
    filename="deco.log",
    format="%(levelname)s %(asctime)s %(message)s",
    datefmt="%x-%X",
    level=logging.INFO,
)

def log_timestamp(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        logging.info(func.__name__)
        result = func(*args, **kwargs)
        return result
    return _wrapper

@log_timestamp
def spam():
    print("Hello from spam()")

# spam = eggs(spam)

spam()

@log_timestamp
def ham(foo):
    print("hello from ham()")
ham("abc")
ham("def")
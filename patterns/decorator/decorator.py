import datetime
import functools

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Executed at {datetime.datetime.now()}')
        func(*args, **kwargs)
    return wrapper

@timer_decorator
def say_something(something):
    print(something)


say_something('Decorator!')

# all good and dandy but
print(say_something.__name__)
# returns 'wrapper' instead of function real name
# to avoid this:
def timer_decorator_modified(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Executed at {datetime.datetime.now()}')
        func(*args, **kwargs)
    return wrapper

@timer_decorator_modified
def say_something_modified(something):
    print(something)

print(say_something_modified('Decorator with functools.wraps'))
print(say_something_modified.__name__)


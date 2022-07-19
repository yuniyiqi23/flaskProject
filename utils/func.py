def use_logger(func):
    def wrapper(*args, **kwargs):
        print("This is {0}".format(func.__name__))
        return func(*args, **kwargs)

    return wrapper


@use_logger
def bar():
    pass


if __name__ == '__main__':
    # bar2 = use_logger(bar)
    bar()

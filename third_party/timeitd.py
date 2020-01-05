from timeit import (
    timeit as tit,
    default_number
)

__version__ = "1.0"

# Timer units
units = {
    "ms": 1e3,
    "us": 1e6,
    "ns": 1e9
}


def timeit(*args, **kwargs):
    """A simple decorator to wrap `timeit.timeit()`.
    Runs the benchmark on the fly.

    Please check `timeit.timeit()` for args. Aside from that,
    `setup` imports the function and `stmt` runs the function at all times,
    so don't use them.

    Also, use `unit` kwarg for result time unit which is either
    ns, us (default) or ms.

    Examples:
        >>> from time import sleep
        >>> @timeit(number=100, unit="ns")
        ... def benchfunc():
        ...     sleep(0.001)
        benchfunc execution avg: 1091.0272400360554 ns
    """
    def wrapper(func):
        # Pull function to globals
        global fun
        fun = func

        # Assign setup and statement args
        kwargs["setup"] = "from timeitd import fun"
        kwargs["stmt"] = "fun()"

        # Get 'unit' kwarg and remove
        unit = kwargs.get("unit")
        kwargs.pop("unit", None)
        if not unit:
            unit = "us"

        # Run
        t = tit(*args, **kwargs)

        # Adjust number for unit
        t *= units["us"]

        # Adjust number for how many times the benchmarked function was run
        num = kwargs.get("number")
        t /= num if num else default_number

        print(func.__name__, "execution avg:", t, unit)
    return wrapper

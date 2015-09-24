
def fibonacci(n):
    """Returns the n-th element in the Fibonacci sequence"""
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


def lucas(n):
    """Returns the n-th element in the Lucas sequence"""
    if(n == 0):
        return 2
    elif(n == 1):
        return 1
    else:
        return(lucas(n - 1) + lucas(n - 2))


def sum_series(n, f=0, s=1):
    """Returns the n-th element in the series. The type series is chosen by
    first:f and second:s values.
    If f = 0, and s = 1, it will use Fibonacci sequence.
    If f = 2, and s = 1, it will use Lucas sequence.
    If other parameters are entered for f and/or s, it will
    use those two values as first two values of a new sequence."""
    if(f == 0 and s == 1):
        return fibonacci(n)
    elif(f == 2 and s == 1):
        return lucas(n)
    else:
        if(n == 0):
            return f
        elif(n == 1):
            return s
        else:
            return (sum_series(n - 1, f, s) + sum_series(n - 2, f, s))


if __name__ == "__main__":
    # These assert statements will test for correctness of corresponding series
    assert(fibonacci(0) == 0)
    assert(fibonacci(1) == 1)
    assert(fibonacci(2) == 1)
    assert(fibonacci(3) == 2)
    assert(fibonacci(4) == 3)
    assert(fibonacci(5) == 5)
    assert(fibonacci(6) == 8)
    assert(fibonacci(7) == 13)
    assert(lucas(0) == 2)
    assert(lucas(1) == 1)
    assert(lucas(2) == 3)
    assert(lucas(3) == 4)
    assert(lucas(4) == 7)
    assert(lucas(5) == 11)
    assert(lucas(6) == 18)
    assert(lucas(7) == 29)
    assert(sum_series(0, 10, 20) == 10)
    assert(sum_series(1, 10, 20) == 20)
    assert(sum_series(2, 10, 20) == 30)
    assert(sum_series(3, 10, 20) == 50)
    assert(sum_series(4, 10, 20) == 80)
    assert(sum_series(5, 10, 20) == 130)
    assert(sum_series(6, 10, 20) == 210)
    assert(sum_series(7, 10, 20) == 340)

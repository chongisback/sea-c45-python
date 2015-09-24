x = 0


def runneth_over():
    global x
    x = x + 1
    print(x)
    runneth_over()

runneth_over()


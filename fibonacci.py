def fibonacci(num: int) -> int:

    a = 0
    b = 1

    for i in range (num):
        c = a
        a, b = a+b, c

    return a


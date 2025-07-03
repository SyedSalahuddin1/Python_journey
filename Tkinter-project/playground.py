def add(*numbers):
    print(numbers[0])
    sums = 0
    for n in numbers:
        sums += n
    return sums
# return(sum(numbers))


print(add(1, 2, 3, 4, 5))


def calculate(n, **kwargs):

    n += kwargs["add"]
    n *= kwargs["multiply"]
    n -= kwargs["subtract"]
    print(n)


calculate(2, add=3, multiply=5, subtract=5)


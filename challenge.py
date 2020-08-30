# multiply method, given a and b will calculate a*b
def multiply(a: int, b: int) -> int:
    # 0 is a absorbing element in multiplication so the result is always 0
    # whenever there's a 0, be it the first operand, second operand or both.
    if a == 0 or b == 0:
        return 0

    # Since a multiplication is a series of sums
    # the variable 'result' will accumulate those sums
    # and its initial value needs to be an identity element (0 in sums)
    # so that it doesn't impact in the final result
    result = 0
    i = 0

    # iterate second operand (b) value times summing the result + first operand (a).
    while i < b:
        result += a
        i += 1

    return result


# power method, given a positive base and exponent will calculate base^exponent
def power(base: int, exponent: int) -> int:
    # By definition, if the exponent is 0 the result is 1 (0 is an absorbing element)
    if exponent == 0:
        return 1

    # Since an exponentiation is a series of multiplications
    # the variable 'result' will accumulate those multiplications
    # and its initial value needs to be an identity element (1 in multiplication)
    # so that it doesn't impact in the final result
    result = 1
    i = 0

    # iterate exponent value times multiplying the result x base.
    while i < exponent:
        result = multiply(result, base)
        i += 1

    return result


if __name__ == "__main__":
    print("Please insert two non-negative integer, x and y")
    try:
        x = int(input("X = "))
        if x < 0:
            raise ValueError
    except ValueError:
        print("Invalid X value")
        exit(-1)

    try:
        y = int(input("Y = "))
        if y < 0:
            raise ValueError
    except ValueError:
        print("Invalid Y value")
        exit(-1)

    print(power(x, y))
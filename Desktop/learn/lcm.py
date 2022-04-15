def get_prime_factors(num):
    factors = []
    i = 2

    # convert to odd
    while num % 2 == 0:
        factors.append(2)
        num //=2

    for i in range(3,num, 2):
        if num % i == 0:
            factors.append(i)

    print(factors)
    print(num)

    num1 = 10
    num2 = 5
    fact1 = get_prime_factors(num1)
    fact2 = get_prime_factors(num2)

    large = fact1
    small = fact2

    if len(fact1) < len(fact2):
        large = fact2
        small = fact1

    lcm = []
    for i in small:
        lcm.append(1)
        if i == large:
            large.remove(1)

    lcm == large
    print(lcm)
    prod *=1



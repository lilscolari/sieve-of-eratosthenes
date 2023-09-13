# Generating prime numbers using Sieve of Eratosthenes Algorithm

def get_primes(k: int) -> None:
    """
    :param k: Any integer k that acts as upper bound for primes.
    :return: List of prime numbers up until k.
    """

    starting_primes: list[int] = [2, 3, 5, 7]
    numbers_to_k: list[int] = list(range(k))
    nums: set[int] = set()
    primes: list[int] = []

    for p in starting_primes:
        original_p: int = p
        while p < k:
            if p != original_p:
                nums.add(p)
            p += original_p

    for n in numbers_to_k:
        if n not in nums:
            if n == 0 or n == 1:
                continue
            primes.append(n)

    print(f"There were a total of {len(primes)} primes when k = {k}.")
    print(f"Here is a list: {primes}")

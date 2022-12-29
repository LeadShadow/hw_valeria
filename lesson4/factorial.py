a = 10
# 5! -> 5 * 4! -> 5 * 4 * 3! -> 5 * 4 * 3 * 2! -> 5 * 4 * 3 * 2 * 1


def factorial(n: int):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)  # return 5 * factorial(4) -> return 5 * 4 * factorial(3)


if __name__ == "__main__":
    print(factorial(5))

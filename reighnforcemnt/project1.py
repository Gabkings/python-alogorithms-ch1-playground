def is_multiple(n,m):
    if m % n == 0:
        return True
    return False

print(is_multiple(3,9))


def is_even(k):
    return False if k & 1 else True

print(is_even(2))
print(is_even(3))
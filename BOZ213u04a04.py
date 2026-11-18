def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


for sayi in range(1, 20):
    if is_prime(sayi):
        print(sayi, end=" ")

print()

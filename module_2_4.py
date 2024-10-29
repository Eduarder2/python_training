numbers = [i for i in range(1, 16)]
primes = list()
not_primes = list()

for num in numbers:
    for divisor in range(2, int(num ** 0.5) + 1):
        if not num % divisor:
            not_primes.append(num)
            break

primes = list(set(numbers) - set(not_primes) - {1})

print(f'{primes}\n{not_primes}')